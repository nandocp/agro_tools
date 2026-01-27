from agro_tools.photoperiod import Photoperiod
import agro_tools.helpers.photoperiod as helpers
from datetime import datetime as dt
from math import radians
import pandas
import pytest
import json

today = dt.now()
params  = {
  "latitude": "-19.91818",
  "longitude": "-43.93705",
  "utc": -3,
  "day": today.day,
  "year": today.year,
  "zenith": ""
}

target_columns = [
  "date",
  "doy",
  "fy_rad",
  "eot_min",
  "decl_rad",
  "decl_deg",
  "to_min",
  "tst_min",
  "sha_deg",
  "zenith_rad",
  "zenith_deg",
  "azimuth_rad",
  "azimuth_deg",
  "ha_rad",
  "ha_deg",
  "snoon",
  "sunrise",
  "sunset",
  "n_hrs"
]

photoperiod = Photoperiod(**params)

class TestPhotoperiod():
  # @pytest.mark.skip
  def test_initialize(self):
    assert isinstance(photoperiod.df, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_base(self):
    assert isinstance(photoperiod.base(), dict)
    for param in params.keys():
      assert(param in photoperiod.base())

  # @pytest.mark.skip
  def test_transform_coordinate(self):
    assert(isinstance(photoperiod.base()["latitude"], float))
    assert(isinstance(photoperiod.base()["longitude"], float))

  # @pytest.mark.skip
  def test_to_json(self):
    json_string = photoperiod.to_json()
    assert(isinstance(json_string, str))
    test_valid_json = json.loads(json_string) and True or False
    assert(test_valid_json)

  # @pytest.mark.skip
  def test_transform_negative_coordinate(self):
    return_value = helpers.transform_coordinate("-19 55 14.99")
    assert(isinstance(return_value, float))
    assert(f"{return_value:.4f}") == "-19.9208"

  # @pytest.mark.skip
  def test_transform_positive_coordinate(self):
    return_value = helpers.transform_coordinate("19 55 14.99")
    assert(isinstance(return_value, float))
    assert(f"{return_value:.4f}") == "19.9208"

  # @pytest.mark.skip
  def test_execute(self):
    tester = photoperiod.execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_return_df(self):
    df_columns = photoperiod.execute().columns.tolist()
    for column in target_columns:
      assert(column) in df_columns

  @pytest.mark.skip # Fix timedelta
  def test_north_pole(self):
    north_pole_params = params | {
      "name": "north_pole",
      "description": "North Pole",
      "latitude": 90.0,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**north_pole_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  @pytest.mark.skip # Fix timedelta
  def test_south_pole(self):
    south_pole_params = params | {
      "name": "south_pole",
      "description": "South pole",
      "latitude": -90.0,    # graus S
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**south_pole_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_arctic_circle(self):
    arctic_circle_params = params | {
      "name": "arctic_circle",
      "edscription": "Arctic Circle",
      "latitude": 66.33,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**arctic_circle_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_cancer_tropic(self):
    cancer_tropic_params = params | {
      "name": "cancer_tropic",
      "description": "Cancer Tropic",
      "latitude": 23.43,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**cancer_tropic_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_equator(self):
    equator_params = params | {
      "name": "equator",
      "description": "Equator",
      "latitude": 0.0,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**equator_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_capricorn_tropic(self):
    capricorn_tropic_params = params | {
      "name": "capricorn_tropic",
      "description": "Capricorn Tropic",
      "latitude": -23.43,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**capricorn_tropic_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_antarctic_circle(self):
    antarctic_circle_params = params | {
      "name": "antarctic_circle",
      "description": "Antarctic Circle",
      "latitude": -66.33,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**antarctic_circle_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_greenwich(self):
    greenwich_params = params | {
      "name": "greenwich",
      "description": "Greenwich",
      "latitude": 51.4769,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**greenwich_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_extreme_west(self):
    extreme_west_params = params | {
      "name": "extreme_west",
      "description": "Extreme west",
      "latitude": 0.0,
      "longitude": -179.999,
      "utc": -12
    }
    tester  = Photoperiod(**extreme_west_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_extreme_east(self):
    extreme_east_params = params | {
      "name": "extreme_east",
      "description": "Extreme east",
      "latitude": 0.0,
      "longitude": 179.999,
      "utc": 12
    }
    tester  = Photoperiod(**extreme_east_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_intl_date_line(self):
    intl_date_line_params = params | {
      "name": "intl_date_line",
      "description": "International date line",
      "latitude": 0.0,
      "longitude": 180.0,
      "utc": 12
    }
    tester  = Photoperiod(**intl_date_line_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_reykjavik_iceland(self):
    city_params = params | {
      "name": "reykjavik_iceland",
      "description": "Reykjavik, Iceland",
      "latitude": 64.14578,
      "longitude": -21.94157,
      "utc": 0
    }
    tester  = Photoperiod(**city_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_singapore(self):
    city_params = params | {
      "name": "singapore",
      "description": "Singapore",
      "latitude": 1.28944,
      "longitude": 103.84998,
      "utc": 8
    }
    tester  = Photoperiod(**city_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_sao_paulo_brasil(self):
    city_params = params | {
      "name": "sao_paulo_brasil",
      "description": "São Paulo, Brasil",
      "latitude": -23.54867,
      "longitude": -46.63825,
      "utc": -3
    }
    tester  = Photoperiod(**city_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_sydney_australia(self):
    city_params = params | {
      "name": "sydney_australia",
      "description": "Sydney, Australia",
      "latitude": -33.85756,
      "longitude": 151.21497,
      "utc": 11
    }
    tester  = Photoperiod(**city_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_la_usa(self):
    city_params = params | {
      "name": "la_usa",
      "description": "Los Angeles, USA",
      "latitude": 34.05224,
      "longitude": -118.24334,
      "utc": -8
    }
    tester  = Photoperiod(**city_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_tokyo_japan(self):
    city_params = params | {
      "name": "tokyo_japan",
      "description": "Tokyo, Japan",
      "latitude": 35.68946,
      "longitude": 139.69172,
      "utc": 9
    }
    tester  = Photoperiod(**city_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_near_pole(self):
    edge_params = params | {
      "name": "near_pole",
      "descripion": "Latitude 89.9°N (near pole)",
      "latitude": 89.9,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**edge_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_near_equator(self):
    edge_params = params | {
      "name": "near_equator",
      "description": "Latitude 0.1° (near equator)",
      "latitude": 0.1,
      "longitude": 0.0,
      "utc": 0
    }
    tester  = Photoperiod(**edge_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def near_intl_date_line(self):
    edge_params = params | {
      "name": "near_intl_date_line",
      "description": "Longitude -179.9° (near international date line)",
      "latitude": 0.0,
      "longitude": -179.9,
      "utc": -12
    }
    tester  = Photoperiod(**edge_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  # @pytest.mark.skip
  def test_utc_plus_14(self):
    edge_params = params | {
      "name": "utc_plus_14",
      "description": "UTC+14 (Line Islands)",
      "latitude": 1.87,
      "longitude": -157.4,
      "utc": 14
    }
    tester  = Photoperiod(**edge_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

  @pytest.mark.skip # fix
  def test_midnight_sun_polar_night(self):
    edge_params = params | {
      "name": "midnight_sun_polar_night",
      "latitude": "78.2232",
      "longitude": "15.6267",
      "utc": 0,
    }
    tester  = Photoperiod(**edge_params).execute()
    assert isinstance(tester, pandas.core.frame.DataFrame)

tests = {
  "extreme_latitude": [
    {
      "name": "north_pole",
      "description": "North Pole",
      "latitude": 90.0,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "arctic_circle",
      "edscription": "Arctic Circle",
      "latitude": 66.33,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "cancer_tropic",
      "description": "Cancer Tropic",
      "latitude": 23.43,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "equator",
      "description": "Equator",
      "latitude": 0.0,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "capricorn_tropic",
      "description": "Capricorn Tropic",
      "latitude": -23.43,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "antarctic_circle",
      "description": "Antarctic Circle",
      "latitude": -66.33,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "south_pole",
      "description": "South pole",
      "latitude": -90.0,    # graus S
      "longitude": 0.0,
      "utc": 0
    }
  ],
  "extreme_longitude": [
    {
      "name": "greenwich",
      "description": "Greenwich",
      "latitude": 51.4769,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "extreme_west",
      "description": "Extreme west",
      "latitude": 0.0,
      "longitude": -179.999,
      "utc": -12
    },
    {
      "name": "extreme_east",
      "description": "Extreme east",
      "latitude": 0.0,
      "longitude": 179.999,
      "utc": 12
    },
    {
      "name": "intl_date_line",
      "description": "International date line",
      "latitude": 0.0,
      "longitude": 180.0,
      "utc": 12
    }
  ],
  "cities": [
    {
      "name": "reykjavik_iceland",
      "description": "Reykjavik, Iceland",
      "latitude": 64.1265,
      "longitude": -21.8174,
      "utc": 0
    },
    {
      "name": "singapore",
      "description": "Singapore",
      "latitude": 1.3521,
      "longitude": 103.8198,
      "utc": 8
    },
    {
      "name": "sao_paulo_brasil",
      "description": "São Paulo, Brasil",
      "latitude": -23.5505,
      "longitude": -46.6333,
      "utc": -3
    },
    {
      "name": "sydney_australia",
      "description": "Sydney, Australia",
      "latitude": -33.8688,
      "longitude": 151.2093,
      "utc": 10
    },
    {
      "name": "la_usa",
      "description": "Los Angeles, USA",
      "latitude": 34.0522,
      "longitude": -118.2437,
      "utc": -8
    },
    {
      "name": "tokyo_japan",
      "description": "Tokyo, Japan",
      "latitude": 35.6762,
      "longitude": 139.6503,
      "utc": 9
    }
  ],
  "edge_cases": [
    {
      "name": "near_pole",
      "descripion": "Latitude 89.9°N (near pole)",
      "latitude": 89.9,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "near_equator",
      "description": "Latitude 0.1° (near equator)",
      "latitude": 0.1,
      "longitude": 0.0,
      "utc": 0
    },
    {
      "name": "near_international_date_line",
      "description": "Longitude -179.9° (near international date line)",
      "latitude": 0.0,
      "longitude": -179.9,
      "utc": -12
    },
    {
      "name": "utc_plus_14",
      "description": "UTC+14 (Line Islands)",
      "latitude": 1.87,
      "longitude": -157.4,
      "utc": 14
    },
    {
      "name": "midnight_sun_polar_night",
      "latitude": "78.2232",
      "longitude": "15.6267",
      "utc": 0,
    }
  ]
}
