from unittest import TestCase
from Calc import Calc


class TestCalc(TestCase):
    def testMinus1(self):
        a = 2
        b = 2
        m = 0
        calc = Calc()
        min = calc.minus(a, b)
        self.assertEqual(m, min)

    def testMinus2(self):
        a = -2
        b = -2
        m = 0
        calc = Calc()
        min = calc.minus(a, b)
        self.assertEqual(m, min)

    def testMinus3(self):
        a = -2
        b = 2
        m = -4
        calc = Calc()
        min = calc.minus(a, b)
        self.assertEqual(m, min)

    def testMinus4(self):
        a = 2
        b = -2
        m = 4
        calc = Calc()
        min = calc.minus(a, b)
        self.assertEqual(m, min)
