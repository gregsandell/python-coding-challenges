# Challenge: write a function that returns true if any pair of numbers in an
# array sum to a target value.
#
# I was presented this challenge on 2020-04-28 by Brian Gilkey for an interivew with
# Cogility.


# export const anyTwoNumsSumToTargetTwoLoops = (arr: number[], sum: number): boolean => {
#   for (let i = 0; i < (arr.length - 1); i++) {
#     for (let j = i + 1; j < arr.length; j++) {
#       if (arr[i] + arr[j] === sum) {
#         return true
#       }
#     }
#   }
#   return false
# }

# Challenge part 2:  solve the problem with recursion
# export const anyTwoNumsSumToTargetRecursive = (arr: number[], sum: number): boolean => {
#   if (arr.length === 1) return false
#   const subArr: number[] = [...arr].splice(1)
#   const outcome: boolean = subArr.some((value: number): boolean => (arr[0] + value) === sum)
#   if (!outcome && subArr.length > 1) return anyTwoNumsSumToTargetRecursive(subArr, sum)
#   return outcome
# }
from array import array
#
def anyTwoNumbersSumToTargetTwoLoops(target: int, arr: array) -> bool:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False
