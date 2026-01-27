from re import search as reSearch
from datetime import date, timedelta, time, datetime as dt
from calendar import isleap
from math import sin, cos, asin, acos, pi, tan, degrees, radians
import pandas
import os

months = [
  'Jan',
  'Fev',
  'Mar',
  'Abr',
  'Mai',
  'Jun',
  'Jul',
  'Ago',
  'Set',
  'Out',
  'Nov',
  'Dez'
]

def build_month_data():
  return { "month": [ month for month in range(1,13) ] }

def build_base_data(kwargs_):
  return {
    **kwargs_,
    "latitude": radians(transform_coordinate(kwargs_["latitude"])),
    "longitude": transform_coordinate(kwargs_["longitude"]),
    "zenith": radians(90.833)
    }

def transform_coordinate(string: str) -> float:
  if not isinstance(string, str):
    string = str(string)

  if (reSearch(r"^[\+|-]?\d+\.\d+", string)):
    return(float(string))

  f_list = [float(s) for s in string.split()]
  mmss = f_list[1]/ 60 + f_list[2] / 3600
  gg = f_list[0]

  if gg < 0:
    return -1 * ((-gg) + mmss)

  return gg + mmss

def build_date(self):
  base = self.base()
  return self.df["month"].apply(lambda month: date(base["year"], month, base["day"]))

def build_day_of_year(self: Self) -> pandas.core.series.Series:
  day = self.base()["day"]
  year = self.base()["year"]
  return self.df["month"].apply(lambda m: date(int(year), m, int(day)).timetuple().tm_yday)

def build_fractional_year(self: Self) -> pandas.core.series.Series:
  hour = 12
  diy = 366 if isleap(self.base()["year"]) else 365 # Days In Year

  gamma_calc = lambda doy: (2 * pi / diy) * (doy - 1 + (hour - 12) / 24)
  return self.df["doy"].apply(gamma_calc)

def build_equation_of_time(self: Self) -> pandas.core.series.Series:
  eot_calc = lambda gamma: 229.18 * (
    0.000075 +\
    0.001868 * cos(gamma) -\
    0.032077 * sin(gamma) -\
    0.014615 * cos(2 * gamma) -\
    0.040849 * sin(2 * gamma)
  )

  return self.df["fy_rad"].apply(eot_calc)

def build_solar_declination(self: Self) -> pandas.core.series.Series:
  sd_calc = lambda fy: 0.006918 -\
    0.399912 * cos(fy) +\
    0.070257 * sin(fy) -\
    0.006758 * cos(2 * fy) +\
    0.000907 * sin(2 * fy) -\
    0.002697 * cos(3 * fy) +\
    0.00148 * sin(3 * fy)

  return self.df["fy_rad"].apply(sd_calc)

def translate_solar_declination_to_degrees(self: Self):
  return self.df["decl_rad"].apply(degrees)

def build_time_offset(self: Self) -> pandas.core.series.Series:
  base = self.base()
  return self.df["eot_min"].apply(
    lambda eot: eot + 4 * base["longitude"] - 60 * base["utc"]
  )

def build_true_solar_time(self: Self) -> pandas.core.series.Series:
  hour = 12
  minutes = 0
  seconds = 0

  return self.df["to_min"].apply(
    lambda t_offset: hour * 60 + minutes + seconds / 60 + t_offset
  )

def build_solar_hour_angle(self: Self) -> pandas.core.series.Series:
  return self.df['tst_min'].apply(lambda tst: (tst / 4.0) - 180)

def build_solar_zenith_rad_angle(self: Self) -> pandas.core.series.Series:
  return self.df.apply(calc_zenith_rad_angle, axis = 1, args=([self.base()["latitude"]]))

def calc_zenith_rad_angle(row, lat):
  cos_phi = (
    sin(lat) * sin(row["decl_rad"]) +
    cos(lat) * cos(row["decl_rad"]) * cos(radians(row["sha_deg"]))
  )

  try:
    return acos(cos_phi)
  except:
    # Garantees that cos_phi is between the allowed range to be acosined
    return acos(max(min(cos_phi, 1.0), -1.0))

def translate_zenith_angle_to_degrees(self):
  return self.df["zenith_rad"].apply(degrees)

def build_solar_azimuth_angle(self: Self) -> pandas.core.series.Series:
  return self.df.apply(calc_azimuth, axis = 1, args=([self.base()["latitude"]]))

def calc_azimuth(row, lat):
  zenith = row["zenith_rad"]

  numerator = sin(lat) * cos(zenith) - sin(row["decl_rad"])
  denominator = cos(lat) * sin(zenith)

  cos_180_minus_theta = - (numerator / denominator)
  if cos_180_minus_theta > 1.0 or cos_180_minus_theta < -1:
    # Ensures result is between -1.0 and 1.0
    cos_180_minus_theta = max(min(cos_180_minus_theta, 1.0), -1.0)

  acos_180_minus_theta = acos(cos_180_minus_theta)
  return 180.0 - degrees(acos_180_minus_theta)

def translate_azimuth_angle_to_radians(self):
  return self.df["azimuth_deg"].apply(radians)

def calc_hour_angle(decl: float, lat: float, zen: float) -> float:
  cos_ha = (cos(zen) / (cos(lat) * cos(decl))) - (tan(lat) * tan(decl))

  if cos_ha >= -1 and cos_ha <= 1:
    return acos(cos_ha)
  else:
    return cos_ha

def build_hour_angle_radians(self: Self) -> pandas.core.series.Series:
  base = self.base()
  lat = base["latitude"]
  zen = base["zenith"]
  return self.df["decl_rad"].apply(calc_hour_angle, args=(lat, zen))

def build_hour_angle_degrees(self: Self) -> pandas.core.series.Series:
  return self.df["ha_rad"].apply(degrees)

def calc_snoon(row: pandas.core.series.Series, kwargs: dict) -> datetime.datetime:
  lon = kwargs["longitude"]
  year = kwargs["year"]
  day = kwargs["day"]
  utc = kwargs["utc"]

  month = row["month"]
  if type(month) != int:
    month = month.astype(int)

  snoon_minutes = 720 - 4 * lon - row["eot_min"]
  return dt(year, month, day) + timedelta(minutes=snoon_minutes, hours=utc)

def build_snoon(self: Self) -> pandas.core.series.Series:
  base = self.base()
  return self.df.apply(calc_snoon, axis=1, kwargs=base)

def calc_sun_moment(row: pandas.core.series.Series, kwargs: dict) -> datetime.datetime:
  lon = kwargs["longitude"]
  day = kwargs["day"]
  utc = kwargs["utc"]
  year = kwargs["year"]

  eot = row["eot_min"]
  ha_deg = row["ha_deg"]

  lon_ha = (lon + ha_deg) if kwargs["type"] == "rise" else (lon - ha_deg)
  moment_minutes = 720 - 4 * lon_ha - eot

  return dt(year, row["month"], day) + timedelta(minutes=moment_minutes, hours=utc)

def build_sun_moment(self: Self, type: str) -> pandas.core.series.Series:
  base = self.base()
  base["type"] = type

  return self.df.apply(calc_sun_moment, axis=1, kwargs=base)

def build_photoperiod(self: Self) -> pandas.core.series.Series:
  photoperiod_calc = lambda row: (
    (row["sunset"] - row["sunrise"]).total_seconds() / 60.0
  ) / 60.0

  return self.df.apply(photoperiod_calc, axis=1)

def debug_dataframe(self: Self) -> None: # pragma: no cover
  if os.environ.get('PYTHON_ENV') == "development":
    print(self.df.info())
    print(self.df)

  # if cos_ha > 1:
  #   # It's polar night
  #   self.df["photoperiod_hrs"] = 0
  #   self.df["photoperiod_mins"] = 0
  # elif cos_ha < -1:
  #   # It's polar day
  #   self.df["photoperiod_hrs"] = 24
  #   self.df["photoperiod_mins"] = 1440
  # else:
  #   ha_rad = acos(cos_ha)
  #   self.df["ha_rad"] = ha_rad
  #   self.df["ha_deg"] = degrees(ha_rad)
