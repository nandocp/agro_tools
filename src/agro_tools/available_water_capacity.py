"""
AvailableWaterCapacity (AWC) represents the maximum available water that a certain type of soil can retain depending on its physical-hydric characteristics, i.e., field capacity moisture (Θcc), moisture of the point of permanent wilting (Θpmp), specific mass of the soil (dg) and of the effective depth of the root system (Zr), where about 80% of the Roots
"""

class AvailableWaterCapacity():
  def __init__(
    self,
    field_capacity,
    permanent_wilting_point,
    bulk_density,
    rooting_depth
  ):
    self.fc = float(field_capacity) / 100.0
    self.pwp = float(permanent_wilting_point) / 100
    self.bd = float(bulk_density)
    self.rz = float(rooting_depth)

  def execute(self):
    return (self.fc - self.pwp) * self.bd * self.rz
