import pytest
import windchill

def test_get_temp_for_0():
  expected = 0
  results = windchill.get_temp("0")
  assert expected == results

