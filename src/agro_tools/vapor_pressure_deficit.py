from numpy import exp

class VaporPressureDeficit():
  def __init__(self, temperature, relative_humidity, unit="kPa", show_unit=False):
    self.unit = unit
    self.temperature = temperature
    self.relative_humidity = relative_humidity
    self.value = None
    self.show_unit = show_unit

  def execute(self):
    e_sat = self.calc_saturation_vapor_pressure()
    e_act = self.calc_actual_vapor_pressure(e_sat)
    vpd = e_sat - e_act

    return self.unit_conversion(vpd)

  def calc_saturation_vapor_pressure(self):
    return 0.611 * exp((
      17.502 * self.temperature) / (self.temperature + 240.97)
    )

  def calc_actual_vapor_pressure(self, e_sat):
    return e_sat * (self.relative_humidity / 100)

  def unit_conversion(self, vpd):
    if self.unit != "kPa":
      vpd = getattr(VaporPressureDeficit, self.unit)(vpd)

    if not self.show_unit:
      return vpd

    return f"{vpd:.3f} {self.unit}"

  def bar(vpd):
    return vpd * 0.01

  def psi(vpd):
    return vpd * 0.1450377377
