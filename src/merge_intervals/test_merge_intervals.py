from merge_intervals import (
    sort_intervals,
    all_intervals_valid,
    itemsAreIntervals,
    mergeIntervals
)

class TestSortIntervals:
    def testCorrectOrder(self):
        assert(sort_intervals([[2,3], [1,2]])) == [[1,2], [2,3]]

class TestAllIntervalsValid:
    def testValidIntervals(self):
        assert(all_intervals_valid([[2,3], [1,2]])) is True
    def testInvalidOrder(self):
        assert(all_intervals_valid([[2,3], [2,1]])) is False

class TestItemsAreIntervals:
    def testValidIntervals(self):
        assert(itemsAreIntervals([[2,3], [2,1]])) is True
    def testValidIntervals(self):
        assert(itemsAreIntervals([[2,3], [2]])) is False

class TestMergeIntervals:
    def test1(self):
        input = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        result = mergeIntervals(input)
        assert(result) == expected
    def test2(self):
        input = [[1, 3], [2, 6], [8, 10], [9, 16], [15, 18], [20,21]]
        expected = [[1, 6], [8, 18], [20,21]]
        result = mergeIntervals(input)
        assert(result) == expected
    def testTouchingIntervalsOverlap(self):
        input = [[1, 2], [2, 3]]
        expected = [[1, 3]]
        result = mergeIntervals(input)
        assert(result) == expected

