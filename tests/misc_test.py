import pytest

def test_validate_yearly_list_error():
  from agro_tools.helpers.utils import validate_yearly_list

  with pytest.raises(ValueError) as excinfo:
    validate_yearly_list(list(range(1,12)))
  assert str(excinfo.value) == "List must have 12 elements"
