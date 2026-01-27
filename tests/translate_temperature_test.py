from agro_tools.translate_temperature import TranslateTemperature
from random import choice
import pytest

class TestTranslateTemperature:
  # @pytest.mark.skip
  def test_initialize(self):
    data = {
      "degrees": "30",
      "show_unit": choice([True, False]),
      "input_output": choice(["c_to_f", "f_to_c"])
    }

    _test = TranslateTemperature(**data)

    assert(_test.degrees) == int(data["degrees"])
    assert(_test.show_unit) == data["show_unit"]
    assert(_test.input_output) == data["input_output"]

  # @pytest.mark.skip
  def test_c_to_f(self):
    _test = TranslateTemperature(
      degrees="10",
      input_output="c_to_f",
      show_unit=False
    )
    assert(_test.execute()) == "50.00"

  # @pytest.mark.skip
  def test_f_to_c(self):
    _test = TranslateTemperature(
      degrees="50",
      input_output="f_to_c",
      show_unit=False
    )
    assert(_test.execute()) == "10.00"

  # @pytest.mark.skip
  def test_k_to_c(self):
    _test = TranslateTemperature(
      degrees="273.15",
      input_output="k_to_c",
      show_unit=False
    )
    assert(_test.execute()) == "0.00"

  # @pytest.mark.skip
  def test_c_to_k(self):
    _test = TranslateTemperature(
      degrees="0",
      input_output="c_to_k",
      show_unit=False
    )
    assert(_test.execute()) == "273.15"

  # @pytest.mark.skip
  def test_f_to_k(self):
    _test = TranslateTemperature(
      degrees="0",
      input_output="f_to_k",
      show_unit=False
    )
    assert(_test.execute()) == "255.37"

  # @pytest.mark.skip
  def test_k_to_f(self):
    _test = TranslateTemperature(
      degrees="0",
      input_output="k_to_f",
      show_unit=False
    )
    assert(_test.execute()) == "-459.67"

  # @pytest.mark.skip
  def test_unknown(self):
    with pytest.raises(ValueError) as excinfo:
      TranslateTemperature(
        degrees="0",
        input_output="salamandra",
        show_unit=False
      ).execute()
    assert str(excinfo.value) == "Unknown format"

  # @pytest.mark.skip
  def test_unit_celsius(self):
    _test = TranslateTemperature(
      degrees="50",
      input_output="f_to_c",
      show_unit=True
    )
    assert(_test.execute()) == "10.00 °C"

  # @pytest.mark.skip
  def test_unit_fahrenheit(self):
    _test = TranslateTemperature(
      degrees="10",
      input_output="c_to_f",
      show_unit=True
    )
    assert(_test.execute()) == "50.00 °F"

  # @pytest.mark.skip
  def test_unit_kelvin(self):
    _test = TranslateTemperature(
      degrees="0",
      input_output="c_to_k",
      show_unit=True
    )
    assert(_test.execute()) == "273.15 K"
