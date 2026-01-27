from agro_tools.water_balance.normal import NormalWaterBalance
import pandas
import pytest

default_params = { "awc": 100 }

a_params = default_params | {
  "precipitation": {
    "1": "271",
    "2": "215",
    "3": "230",
    "4": "119",
    "5": "20",
    "6": "9",
    "7": "5",
    "8": "12",
    "9": "30",
    "10": "123",
    "11": "223",
    "12": "280"
  },
  "pet": {
    "1": "116",
    "2": "97",
    "3": "104",
    "4": "88",
    "5": "78",
    "6": "63",
    "7": "62",
    "8": "90",
    "9": "94",
    "10": "109",
    "11": "106",
    "12": "106"
  }
}

b_params = default_params | {
  "precipitation": {
    "1": "45",
    "2": "58",
    "3": "100",
    "4": "115",
    "5": "104",
    "6": "122",
    "7": "133",
    "8": "74",
    "9": "47",
    "10": "33",
    "11": "18",
    "12": "22"
  },
  "pet": {
    "1": "96",
    "2": "80",
    "3": "94",
    "4": "75",
    "5": "76",
    "6": "63",
    "7": "60",
    "8": "63",
    "9": "60",
    "10": "83",
    "11": "89",
    "12": "98"
  }
}

c_params = default_params | {
  "precipitation": {
    "1": "72",
    "2": "90",
    "3": "148",
    "4": "82",
    "5": "29",
    "6": "10",
    "7": "13",
    "8": "4",
    "9": "6",
    "10": "21",
    "11": "50",
    "12": "84"
  },
  "pet": {
    "1": "153",
    "2": "139",
    "3": "143",
    "4": "121",
    "5": "116",
    "6": "97",
    "7": "103",
    "8": "106",
    "9": "127",
    "10": "167",
    "11": "174",
    "12": "157"
  }
}

d_params = default_params | {
  "precipitation": {
    "1": "143",
    "2": "148",
    "3": "121",
    "4": "118",
    "5": "131",
    "6": "129",
    "7": "153",
    "8": "166",
    "9": "207",
    "10": "167",
    "11": "141",
    "12": "162"
  },
  "pet": {
    "1": "105",
    "2": "92",
    "3": "90",
    "4": "64",
    "5": "44",
    "6": "35",
    "7": "36",
    "8": "43",
    "9": "47",
    "10": "68",
    "11": "82",
    "12": "100"
  }
}

class TestNormalWaterBalance():
  # @pytest.mark.skip
  def test_initialize(self):
    tester = NormalWaterBalance(**c_params)
    assert isinstance(tester.df, pandas.core.frame.DataFrame)
    assert('month' in tester.df)
    assert('p' in tester.df)
    assert(tester.df['p'].isna().sum()) == 0
    assert(tester.df['p'].dtype == 'float64')

  # @pytest.mark.skip
  def test_execute_a_params(self):
    tester = NormalWaterBalance(**a_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_execute_b_params(self):
    tester = NormalWaterBalance(**b_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_execute_c_params(self):
    tester = NormalWaterBalance(**c_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_execute_d_params(self):
    tester = NormalWaterBalance(**d_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_columns_creation(self):
    tester = NormalWaterBalance(**b_params)
    assert('p_pet' not in tester.df)
    tester.create_p_pet_column()
    assert('p_pet' in tester.df)
    tester.calc_p_pet_sum()
    assert('start_calc' not in tester.df)
    tester.create_start_calc_column()
    assert('start_calc' in tester.df)
    tester.set_first_mcwd_sto()
    tester.populate_mcwd_sto_columns()
    assert('delta_sto' not in tester.df)
    tester.create_delta_sto_column()
    assert('delta_sto' in tester.df)
    assert('aet' not in tester.df)
    tester.create_aet_column()
    assert('aet' in tester.df)
    assert('def' not in tester.df)
    tester.create_def_column()
    assert('def' in tester.df)
    assert('sur' not in tester.df)
    tester.create_sur_column()
    assert('sur' in tester.df)
