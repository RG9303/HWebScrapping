import re

regex = r"[-+]?(?:\d*\.\d+|\d+)"

def get_number_from_string(string: str, return_zero: bool = False):
  if string:
    # number_list = list(filter(str.isdigit, string.strip()))
    number_list = re.findall(regex, string)
    number = ''.join(number_list)

    if is_int(number):
      return int(number)
    elif is_float(number):
      return float(number)
  
  return 0 if return_zero else None

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def is_int(value):
  try:
    int(value)
    return True
  except:
    return False