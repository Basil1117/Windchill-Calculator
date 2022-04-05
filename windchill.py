# windchill.py
# some functions to work with the Windchill calculator to make sure
# inputs are correct and the calculation works as well as displaying
# the output in a well-formatted display

def get_results(temp, wind):
  """ returns the results of trying to calculate wind chill"""
  temp = get_temp(temp)
  results = str(temp)

  return results

def get_temp(temp):
  """receives a temp (str) and returns an integer or error message"""
  if not temp:
    return "Temperature was missing."

    # if there are no errors (convert to int)
  return int(temp)