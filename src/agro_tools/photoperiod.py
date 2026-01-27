# Script based on https://gml.noaa.gov/grad/solcalc/solareqns.PDF

import agro_tools.helpers.photoperiod as helpers
import pandas as pd
from math import degrees

class Photoperiod():
  def __init__(self, **kwargs):
    self.df = pd.DataFrame(helpers.build_month_data())
    self.__base_data = helpers.build_base_data(kwargs)

  def execute(self):
    self.df["date"] = helpers.build_date(self)
    self.df["doy"] = helpers.build_day_of_year(self)
    self.df["fy_rad"] = helpers.build_fractional_year(self)
    self.df["eot_min"] = helpers.build_equation_of_time(self)
    self.df["decl_rad"] = helpers.build_solar_declination(self)
    self.df["decl_deg"] = helpers.translate_solar_declination_to_degrees(self)
    self.df["to_min"] = helpers.build_time_offset(self)
    self.df["tst_min"] = helpers.build_true_solar_time(self)
    self.df["sha_deg"] = helpers.build_solar_hour_angle(self)
    self.df["zenith_rad"] = helpers.build_solar_zenith_rad_angle(self)
    self.df["zenith_deg"] = helpers.translate_zenith_angle_to_degrees(self)
    self.df["azimuth_deg"] = helpers.build_solar_azimuth_angle(self)
    self.df["azimuth_rad"] = helpers.translate_azimuth_angle_to_radians(self)
    self.df["ha_rad"] = helpers.build_hour_angle_radians(self)
    self.df["ha_deg"] = helpers.build_hour_angle_degrees(self)
    self.df["snoon"] = helpers.build_snoon(self)
    self.df["sunrise"] = helpers.build_sun_moment(self, "rise")
    self.df["sunset"] = helpers.build_sun_moment(self, "set")
    self.df["n_hrs"] = helpers.build_photoperiod(self)

    helpers.debug_dataframe(self)

    return self.df

  def base(self):
    return self.__base_data

  def to_json(self):
    return self.df.to_json()
