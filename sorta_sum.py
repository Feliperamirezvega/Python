# Logic-1 > sorta_sum

"""

Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21

https://codingbat.com/prob/p116620
"""
def sorta_sum(a, b):

  if 10 <= (a + b)<= 20:
    return 20
  else:
    return (a + b)
