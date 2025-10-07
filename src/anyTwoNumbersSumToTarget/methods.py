# Challenge: write a function that returns true if any pair of numbers in an
# array sum to a target value.
#
# I was presented this challenge on 2020-04-28 by Brian Gilkey for an interivew with
# Cogility.


from array import array
def anyTwoNumbersSumToTargetTwoLoops(arr: array, target: int) -> bool:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

# Challenge part 2:  solve the problem with recursion
def anyTwoNumsSumToTargetRecursive(sum: int, arr: array) -> bool:
  if len(arr) == 1: return False;
  subArr: array = arr[1:];
  del arr[1:];
  outcome: bool = any((arr[0] + value) == sum for value in subArr);
  if not outcome and len(subArr) > 1:
      return anyTwoNumsSumToTargetRecursive(sum, subArr);
  return outcome;


