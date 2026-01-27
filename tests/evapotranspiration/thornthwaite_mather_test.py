from agro_tools.evapotranspiration.thornthwaite_mather import ThornthwaiteMatherEvapoT
from datetime import datetime as dt
import pandas
import numpy as np
import pytest

today = dt.now()

default_params = {
  "cad": 100,
  "day": today.day,
  "year": today.year
}
with_pet_params = default_params.copy() | {
  "pet": {
    "1": "106.976",
    "2": "92.3299",
    "3": "92.1816",
    "4": "70.4095",
    "5": "53.8174",
    "6": "41.0941",
    "7": "40.6553",
    "8": "47.9507",
    "9": "63.4355",
    "10": "81.0741",
    "11": "90.2971",
    "12": "100.1089"
  }
}

without_pet_params = default_params.copy() | {
  "temperature": {
    "1": 22.1,
    "2": 22.0,
    "3": 21.4,
    "4": 19.5,
    "5": 17.1,
    "6": 15.4,
    "7": 15.0,
    "8": 16.0,
    "9": 18.2,
    "10": 19.8,
    "11": 20.7,
    "12": 21.3
  },
  "latitude": "-19.91818",
  "longitude": "-43.93705",
  "utc": -3
}

without_pet_params_with_n = without_pet_params.copy()
without_pet_params_with_n['n_hrs'] = {
    "1": 13.275,
    "2": 12.8,
    "3": 12.2,
    "4": 11.6,
    "5": 11.1625,
    "6": 10.8625,
    "7": 10.9625,
    "8": 11.3625,
    "9": 12.0,
    "10": 12.5375,
    "11": 13.2,
    "12": 13.375
  }

class TestThorntheaiteMatherEvapoT():
  # @pytest.mark.skip
  def test_initialize(self):
    tester = ThornthwaiteMatherEvapoT(**with_pet_params)
    assert isinstance(tester.df, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_execute_with_pet_params(self):
    tester = ThornthwaiteMatherEvapoT(**with_pet_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)
    assert(tester['pet'].dtype == 'float64')

  # @pytest.mark.skip
  def test_execute_without_pet_params(self):
    tester = ThornthwaiteMatherEvapoT(**without_pet_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)
    assert(tester['pet'].dtype == 'float64')

  # @pytest.mark.skip
  def test_execute_without_pet_params_with_n(self):
    tester = ThornthwaiteMatherEvapoT(**without_pet_params_with_n).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)
    assert(tester['pet'].dtype == 'float64')

  # @pytest.mark.skip
  def test_calc_pet(self):
    tester = ThornthwaiteMatherEvapoT(**without_pet_params)
    tester.insert_days_of_month()
    tester.insert_temperature()
    tester.calc_thermal_index()
    tester.calc_standard_pet()
    assert('pet' not in tester.df)
    tester.calc_pet()
    assert('pet' in tester.df)
    assert(tester.df['pet'].isna().sum()) == 0
