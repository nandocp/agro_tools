from agro_tools.vapor_pressure_deficit import VaporPressureDeficit
from random import choice

params_no_unit = {
  "unit": "kPa",
  "temperature": 25,
  "relative_humidity": 75,
  "show_unit": False
}

params_unit = {
  "unit": "kPa",
  "temperature": 25,
  "relative_humidity": 75,
  "show_unit": True
}



class TestVaporPressureDeficit():
  def test_execute_kPa_not_showing_unit(self):
    tester = VaporPressureDeficit(**params_no_unit).execute()
    assert(tester) == 0.7914865996401641

  def test_execute_psi_not_showing_unit(self):
    params_psi = params_no_unit.copy()
    params_psi['unit'] = 'psi'
    tester = VaporPressureDeficit(**params_psi).execute()
    assert(tester) == 0.11479542583167504

  def test_execute_bar_not_showing_unit(self):
    params_bar = params_no_unit.copy()
    params_bar['unit'] = 'bar'
    tester = VaporPressureDeficit(**params_bar).execute()
    assert(tester) == 0.007914865996401642

  def test_execute_kPa_showing_unit(self):
    tester = VaporPressureDeficit(**params_unit).execute()
    assert(tester) == "0.791 kPa"

  def test_execute_psi_showing_unit(self):
    params_psi = params_unit.copy()
    params_psi['unit'] = 'psi'
    tester = VaporPressureDeficit(**params_psi).execute()
    assert(tester) == "0.115 psi"

  def test_execute_bar_showing_unit(self):
    params_bar = params_unit.copy()
    params_bar['unit'] = 'bar'
    tester = VaporPressureDeficit(**params_bar).execute()
    assert(tester) == "0.008 bar"
