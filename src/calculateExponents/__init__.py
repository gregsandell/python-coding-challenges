from functools import reduce
def calculateExp(base:int, pow: int) -> float:
  if pow == 0:
    return 1
  if pow == 1:
    return base
  myPow = -pow if pow < 0 else pow #  abs(pow) also works
  countArray = range(myPow - 1)
  result = reduce(lambda accum, _: accum * base, countArray, base)
  return result if pow > 1 else 1 / result
