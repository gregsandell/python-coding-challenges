import unittest
from . methods import anyTwoNumbersSumToTargetTwoLoops, anyTwoNumsSumToTargetRecursive
from array import array


class MyTwoLoopsTestCase(unittest.TestCase):
    test_array1 = array('i', [2, 6, 46, 3])
    test_array2 = array('i', [2, 7, 46, 3])
    result1 = anyTwoNumbersSumToTargetTwoLoops(test_array1, 8)
    result2 = anyTwoNumbersSumToTargetTwoLoops(test_array2, 8)

    def test_callSucceeds(self):
        self.assertEqual(self.result1, True)  # add assertion here

    def test_callFails(self):
        self.assertEqual(self.result2, False)  # add assertion here

class MyRecursionTestCase(unittest.TestCase):
    test_array1 = array('i', [2, 6, 46, 3])
    test_array2 = array('i', [2, 7, 46, 3])
    result1 = anyTwoNumsSumToTargetRecursive(8, test_array1)
    result2 = anyTwoNumsSumToTargetRecursive(8, test_array2)

    def test_callSucceeds(self):
        self.assertEqual(self.result1, True)  # add assertion here

    def test_callFails(self):
        self.assertEqual(self.result2, False)  # add assertion here

def create_my_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(MyTwoLoopsTestCase))
    suite.addTests(loader.loadTestsFromTestCase(MyRecursionTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(create_my_suite())
