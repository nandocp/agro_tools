# https://soilwater.github.io/pynotes-agriscience/basic_concepts/if_statement.html#example-3-climate-classification-based-on-aridity-index

# traduções = {
#   "awc - available water capacity": "cad",
#   "mcwd - maximum cumulative water deficit": "nac",
#   "pet - potential evapotranspiration": "etp",
#   "aet - actual evapotranspiration": "etr",
#   "sto - storage": "arm",
#   "def - water deficit": "def",
#   "sur - water surplus": "exc"
# }

from agro_tools.helpers.utils import build_month_data, validate_yearly_list
import pandas
from numpy import log, exp, absolute

class NormalWaterBalance():
  def __init__(self, precipitation, pet, **kwargs):
    self.initialize_df(precipitation, pet)
    self.p_pet_sum = { "total": 0, "positive": 0, "negative": 0 }
    self.params = kwargs

  def execute(self: Self) -> pandas.core.frame.DataFrame:
    self.create_p_pet_column()
    self.calc_p_pet_sum()
    self.create_start_calc_column()
    self.set_first_mcwd_sto()
    self.populate_mcwd_sto_columns()
    self.create_delta_sto_column()
    self.create_aet_column()
    self.create_def_column()
    self.create_sur_column()

    return self.df

  def initialize_df(self: Self, precipitation: dict, pet: dict) -> None:
    self.df = pandas.DataFrame(build_month_data())

    precipitation_values = precipitation.values()
    validate_yearly_list(precipitation_values)
    self.df['p'] = precipitation_values
    self.df['p'] = self.df['p'].astype('float64')

    pet_values = pet.values()
    validate_yearly_list(pet_values)
    self.df['pet'] = pet_values
    self.df['pet'] = self.df['pet'].astype('float64')

    self.df['mcwd_sto_ok'] = False
    for col in ['mcwd', 'sto']:
      self.df[col] = 0.0

  def create_p_pet_column(self):
    p_pet = lambda row: row['p'] - row['pet']
    self.df['p_pet'] = self.df.apply(p_pet, axis=1)

  def create_start_calc_column(self):
    self.df['start_calc'] = self.df.apply(self.define_start_sto, axis=1)

  def create_sur_column(self: self):
    awc = self.params['awc']
    sur = lambda row: row['p_pet'] - row['delta_sto'] if row['sto'] == awc else 0.0
    self.df['sur'] = self.df.apply(sur, axis = 1)

  def create_def_column(self: Self):
    def_ = lambda row: row['pet'] - row['aet']
    self.df['def'] = self.df.apply(def_, axis = 1)

  def create_aet_column(self: Self):
    aet = lambda row: row['pet'] if row['p_pet'] >= 0 else row['p'] + absolute(row['delta_sto'])
    self.df['aet'] = self.df.apply(aet, axis = 1)

  def delta_sto(self, row):
    index = row.name
    previous_index = index - 1
    if index == 0:
      previous_index = 11

    previous_row = self.df.iloc[previous_index]
    return row['sto'] - previous_row['sto']

  def create_delta_sto_column(self: Self) -> None:
    self.df['delta_sto'] = self.df.apply(self.delta_sto, axis = 1)

  def set_first_mcwd_sto(self: Self) -> None:
    first_index = self.get_first_calc_index()
    if not first_index:
      return

    if first_index == 0:
      first_index = 11
    else:
      first_index -= 1

    awc = self.params['awc']
    p_pet_total = self.p_pet_sum['total']
    p_pet_positive = self.p_pet_sum['positive']
    p_pet_negative = self.p_pet_sum['negative']
    if p_pet_total >= 0 or (p_pet_total < 0 and p_pet_positive >= awc):
      self.df.at[first_index, 'sto'] = awc
      self.df.at[first_index, 'mcwd_sto_ok'] = True
    else:
      mcwd = awc * log((p_pet_positive / awc) / (1 - exp(p_pet_negative / awc)))
      self.df.at[first_index, 'mcwd'] = mcwd
      self.df.at[first_index, 'sto'] = self.calc_sto(mcwd = mcwd, awc = awc)
      self.df.at[first_index, 'mcwd_sto_ok'] = True

  def get_previous_row(self: Self, current_row: pandas.core.series.Series) -> list:
    current = current_row.name
    previous = current - 1
    if current == 0:
      previous = 11

    return self.df.iloc[previous]

  def define_start_sto(self: Self, row: pandas.core.series.Series) -> bool:
    previous_row = self.get_previous_row(row)
    current_p_pet = row['p_pet']
    previous_p_pet = previous_row['p_pet']
    if current_p_pet < 0 and previous_p_pet >= 0:
      return True

    return False

  def populate_mcwd_sto_columns(self):
    awc = self.params['awc']

    if len(self.df[self.df['p_pet'] >= 0]['p_pet']) == 12:
      self.df['mcwd'] = 0
      self.df['sto'] = awc
    else:
      order = self.set_mcwd_sto_order()

      for index in order:
        current_row = self.df.iloc[index]

        if not current_row["mcwd_sto_ok"]:
          previous_index = index - 1
          if index == 0:
            previous_index = 11
          previous_row = self.df.iloc[previous_index]

        p_pet = current_row['p_pet']
        sto = 0
        mcwd = 0

        if p_pet >= 0:
          sto = previous_row['sto'] + p_pet
          mcwd = self.calc_mcwd(sto = sto, awc = awc)
        else:
          mcwd = previous_row['mcwd'] + p_pet
          sto = self.calc_sto(mcwd = mcwd, awc = awc)

        if sto >= awc:
          sto = awc
          mcwd = 0

        self.df.at[index, 'sto'] = sto
        self.df.at[index, 'mcwd'] = mcwd

  def calc_sto(self: Self, mcwd: float, awc: float) -> float:
    return awc * exp(mcwd / awc)

  def calc_mcwd(self: Self, sto: float, awc: float) -> float:
    return awc * log(sto / awc)

  def get_first_calc_index(self):
    index_values = self.df[self.df['start_calc'] == True].index.values
    if len(index_values) == 0:
      return

    return int(index_values[0])

  def set_mcwd_sto_order(self):
    first_index = self.get_first_calc_index()
    return list(range(first_index, 12)) + list(range(0,first_index))

  def calc_p_pet_sum(self: Self) -> float:
    self.p_pet_sum['total'] = self.df['p_pet'].sum()
    self.p_pet_sum['positive'] = self.df[self.df['p_pet'] >= 0]['p_pet'].sum()
    self.p_pet_sum['negative'] = self.df[self.df['p_pet'] < 0]['p_pet'].sum()
