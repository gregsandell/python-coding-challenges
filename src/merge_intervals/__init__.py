# TODO represent intervals this way:
# from typing import List, Tuple
#
# Interval = Tuple[int, int]  # exactly 2 ints
# intervals: List[Interval] = [(1, 3), (5, 8)]
# Tuple[int, int] means exactly two integers, unlike list[int].
#
# List[Interval] is then a list of 2-element tuples.

def sort_intervals(intervals: list[list[int]]) -> list[list[int]]:
    return sorted(intervals, key=lambda interval: interval[0])

def all_intervals_valid(nums):
    return all(interval[1] >= interval[0] for interval in nums)

def itemsAreIntervals(intervals: list[list[int]]):
    return all(len(interval) == 2 for interval in intervals)

def mergeIntervals(_nums: list[list[int]]) -> list[list[int]]:
    result = []
    if len(_nums) == 0:
        return result
    nums = sort_intervals(_nums)
    current = nums[0]


    for i, value in enumerate(nums, start=1):
        next = value
        # Using <= here allows "touching intervals" (e.g. [[1,2],[2,3]])
        # to merge (e.g. [[1,3]]).  To disallow this change <= to <.
        if next[0] <= current[1]:
            # max(current[1], next[1]) ensures the merged interval
            # covers the entire range of both overlapping intervals:
            # 1. Take the earliest start
            # 2. Take the latest end
            current = [current[0], max(current[1], next[1])]
        else:
            result.append(current)
            current = next

    result.append(current)
    return result
