from unittest import TestCase
from Calc import Calc


class TestCalc(TestCase):
    def testAdd1(self):
        a = 1
        b = 2
        s = 3
        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd2(self):
        a = 1
        b = -2
        s = -1
        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd3(self):
        a = -1
        b = 2
        s = 1
        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)

    def testAdd4(self):
        a = -1
        b = -2
        s = -3
        calc = Calc()
        sum = calc.add(a, b)
        self.assertEqual(s, sum)
