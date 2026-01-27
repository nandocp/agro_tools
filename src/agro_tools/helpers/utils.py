def build_month_data():
  return { "month": [ month for month in range(1,13) ] }

def validate_yearly_list(_list: list) -> bool:
  if not len(_list) == 12:
    raise ValueError("List must have 12 elements")

  return True
