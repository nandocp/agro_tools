class BaseEvapoT():
  def __init__(self: Self, **kwargs: dict):
    self.df = pandas.DataFrame(build_month_data())
    self.__params = kwargs

  def params(self: Self) -> dict:
    return self.__params
