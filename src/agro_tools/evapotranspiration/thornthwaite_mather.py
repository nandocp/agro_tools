# https://etcalc.hydrotools.tech/pageMain.php
# https://docs.fct.unesp.br/docentes/geo/tadeu/Climatologia/evapotranspiracao_3.pdf

import pandas
from agro_tools.helpers.utils import build_month_data, validate_yearly_list
from math import pow
from calendar import monthrange

class ThornthwaiteMatherEvapoT():
  def __init__(self: Self, **kwargs):
    self.df = pandas.DataFrame(build_month_data())
    self.__params = kwargs

  def params(self: Self) -> dict:
    return self.__params

  def execute(self: Self) -> pandas.core.frame.DataFrame:
    pet = self.params().get('pet')

    if pet:
      values = pet.values()
      validate_yearly_list(values)
      self.df['pet'] = values
      self.df['pet'] = self.df['pet'].astype('float64')
    else:
      self.insert_days_of_month()
      self.insert_temperature()
      self.calc_thermal_index()
      self.calc_standard_pet()
      self.calc_pet()

    return self.df

  def calc_pet(self: Self) -> None:
    n_params = self.params().get('n_hrs')
    if n_params:
      self.insert_n_hrs(n_params)
    else:
      self.calc_n_hrs()

    calc_correction_factor = lambda row: (row['n_hrs'] / 12) * (row['dom'] / 30)
    self.df['cf'] = self.df.apply(calc_correction_factor, axis=1)
    self.df['pet'] = self.df.apply(lambda row: row['s_pet'] * row['cf'], axis=1)

  def insert_days_of_month(self: Self) -> None:
    self.df['dom'] = self.df['month'].apply(lambda month: monthrange(self.params().get('year'), month)[1])

  def insert_temperature(self: Self) -> None:
    temps = self.params().get('temperature').values()
    validate_yearly_list(temps)
    self.df['temperature_c'] = temps

  def calc_thermal_index(self: Self) -> None:
    self.df['i'] = self.df['temperature_c'].apply(
      lambda temp: pow((0.2 * temp), 1.514)
    )

  def calc_standard_pet(self: Self):
    i_sum = self.df['i'].sum()
    heat_index = ((6.75 * pow(10, -7)) * pow(i_sum, 3)) - \
      ((7.71 * pow(10, -5)) * pow(i_sum, 2)) + \
      ((1.7912 * pow(10, -2)) * i_sum) + \
      (0.49239)
    self.df['s_pet'] = self.df['temperature_c'].apply(lambda temp: 16 * pow(((10 * temp) / i_sum), heat_index))

  def insert_n_hrs(self: Self, n_params: dict) -> None:
    n_values = n_params.values()
    validate_yearly_list(n_values)
    self.df['n_hrs'] = n_values
    self.df['n_hrs'] = self.df['n_hrs'].astype('float64')

  def calc_n_hrs(self):
    from agro_tools.photoperiod import Photoperiod

    photperiod_params = {
      "longitude": self.params().get('longitude'),
      "latitude": self.params().get('latitude'),
      "day": self.params().get('day'),
      "year": self.params().get('year'),
      "utc": self.params().get('utc')
    }

    photoperiod = Photoperiod(**photperiod_params).execute()
    self.df = self.df.join(photoperiod['n_hrs'])
