from agro_tools.available_water_capacity import AvailableWaterCapacity

params = {
  "field_capacity": "32",
  "permanent_wilting_point": "20",
  "bulk_density": "1.3",
  "rooting_depth": "500"
}

class TestAvailableWaterCapacity():
  def test_execute(self):
    tester = AvailableWaterCapacity(**params).execute()
    assert(isinstance(tester, float))
    assert(tester) == 78.0
