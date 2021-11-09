from unittest import TestCase
from Calc import Calc


class TestCalc(TestCase):
    def testDiv1(self):
        a = 18
        b = 3
        d = 6
        calc = Calc()
        div = calc.division(a, b)
        self.assertEqual(d, div)

    def testDiv2(self):
        a = -18
        b = 3
        d = -6
        calc = Calc()
        div = calc.division(a, b)
        self.assertEqual(d, div)

    def testDiv3(self):
        a = 18
        b = -3
        d = -6
        calc = Calc()
        div = calc.division(a, b)
        self.assertEqual(d, div)

    def testDiv4(self):
        a = -18
        b = -3
        d = 6
        calc = Calc()
        div = calc.division(a, b)
        self.assertEqual(d, div)

    def testDiv5(self):
        a = -18
        b = 0
        d = None
        calc = Calc()
        div = calc.division(a, b)
        self.assertEqual(d, div)
