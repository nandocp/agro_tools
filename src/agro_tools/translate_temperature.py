class TranslateTemperature():
  def __init__(self: Self, degrees: str, show_unit: bool =False, input_output: str ='c_to_f'):
    self.degrees = float(degrees)
    self.show_unit = show_unit
    self.input_output = input_output.lower()

  def execute(self: Self) -> float | str:
    new_degree = self.calculate()
    return self.format(new_degree)

  def calculate(self: Self) -> float:
    current = self.degrees
    new_degree = ""

    match self.input_output:
      case 'c_to_f':
        new_degree = (current * 1.8) + 32
      case 'f_to_c':
        new_degree = (current - 32) / 1.8
      case 'k_to_c':
        new_degree = current - 273.15
      case 'c_to_k':
        new_degree = current + 273.15
      case 'f_to_k':
        new_degree = 5/9 * (current - 32) + 273.15
      case 'k_to_f':
        new_degree = 9/5 * (current - 273.15) + 32
      case _:
        raise ValueError("Unknown format")

    return new_degree

  def format(self: Self, new_degree: float) -> str:
    new_degree = f"{new_degree:.2f}"

    if self.show_unit:
      new_degree = f"{new_degree} {self.unit()}"

    return new_degree

  def unit(self: Self) -> str:
    out_u = self.input_output.split('_')[-1]
    base = out_u[0].upper()

    if out_u == 'k':
      return base

    return f"°{base}"
