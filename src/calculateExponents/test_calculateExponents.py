import unittest
from typing import TypedDict
from calculateExponents import  calculateExp
class CalcDataShape(TypedDict):
  base: int
  pow: int
  output: float

class ExponentsTest(unittest.TestCase):
    testData: list[CalcDataShape] = [
        { "base": 5, "pow": 1, "output": 5 },
        { "base": 5, "pow": 2, "output": 25 },
        { "base": 5, "pow": 3, "output": 125 },
        { "base": 5, "pow": -3, "output": 0.008 },
        { "base": 5, "pow": -1, "output": 0.2 },
        { "base": 5, "pow": -2, "output": 0.04 },
        { "base": 5, "pow": -3, "output": 0.008 },
        { "base": 5, "pow": 0, "output": 1 },
    ]
    def test_loopTestCases(self):
        for record in self.testData:
            self.assertEqual(calculateExp(record["base"], record["pow"]), record["output"])
