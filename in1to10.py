# Logic-1 > in1to10

"""
Given a number n, return True if n is in the range 1..10, 
inclusive. Unless outside_mode is True, in which case return 
True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True

https://codingbat.com/prob/p158497
"""

def in1to10(n, outside_mode):
  if outside_mode:
    if 1 >= n or n >= 10:
      return True
    else:
      return False
  else:
    if n in range(1, 11):
      return True
    else:
      return False