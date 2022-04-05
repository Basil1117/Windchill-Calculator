import pytest
import windchill

def test_get_temp_for_0():
  expected = 0
  results = windchill.get_temp("0")
  assert expected == results

def test_get_temp_for_empty_string():
  expected = "Temperature was missing"
  results = windchill.get_temp("")
  assert expected == results

def test_get_temp_for_negative_5():
  expected = -5
  results = windchill.get_temp("-5")
  assert expected == results