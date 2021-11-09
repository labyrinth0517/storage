from unittest import TestCase
from Calc import Calc


class TestCalc(TestCase):
    def testMulti1(self):
        a = 2
        b = 3
        m = 6
        calc = Calc()
        mul = calc.multiply(a, b)
        self.assertEqual(m, mul)

    def testMulti2(self):
        a = -2
        b = 3
        m = -6
        calc = Calc()
        mul = calc.multiply(a, b)
        self.assertEqual(m, mul)

    def testMulti3(self):
        a = 2
        b = -4
        m = -8
        calc = Calc()
        mul = calc.multiply(a, b)
        self.assertEqual(m, mul)

    def testMulti4(self):
        a = -2
        b = -3
        m = 6
        calc = Calc()
        mul = calc.multiply(a, b)
        self.assertEqual(m, mul)

    def testMulti5(self):
        a = -2
        b = 0
        m = 0
        calc = Calc()
        mul = calc.multiply(a, b)
        self.assertEqual(m, mul)
