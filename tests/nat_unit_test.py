import unittest

from src.arithmetic.nat import Nat
from src.arithmetic.succ import Succ
from src.arithmetic.zero import Zero

class NatUnitTest(unittest.TestCase):
    def test_to_string_zero(self):
        self.assertEqual(str(Zero()), '0')

    def test_to_representation_zero(self):
        self.assertEqual(repr(Zero()), '0')

    def test_to_string_one(self):
        self.assertEqual(str(Succ(Zero())), 'S(0)')

    def test_to_representation_one(self):
        self.assertEqual(repr(Succ(Zero())), 'S(0)')

    def test_equals_same(self):
        two1 = Succ(Succ(Zero()))
        two2 = Succ(Succ(Zero()))
        self.assertEqual(two1, two2)
        # self.assertTrue(two1 == two2)
        # self.assertTrue(two1.equals(two2))

    def test_equals_different(self):
        one = Succ(Zero())
        two = Succ(Succ(Zero()))
        # self.assertFalse(two == one)
        self.assertFalse(one.equals(two))
        self.assertFalse(two.equals(one))
        # self.assertFalse(one == two)
        # self.assertFalse(two == one)

    def test_equals_non_nat(self):
        one = Succ(Zero())
        # self.assertTrue(one.equals(one))
        # self.assertFalse(one == object())
        self.assertFalse(one.equals(object))

    def test_zero_is_zero(self):
        zero = Zero()
        # self.assertTrue(zero.equals(zero))
        self.assertTrue(zero.is_zero())
        self.assertFalse(zero.is_one())

    def test_one_is_one(self):
        one = Succ(Zero())
        self.assertFalse(one.is_zero())
        self.assertTrue(one.is_one())

    def test_add(self):
        zero = Zero()
        two = Succ(Succ(zero))
        three = Succ(two)
        five = Succ(Succ(three))
        # self.assertEqual(two, zero + two)
        # self.assertEqual(two, zero.add(two))
        # self.assertEqual(five, two + three)
        self.assertEqual(five, two.add(three))

    def test_subtract(self):
        zero = Zero()
        one = Succ(zero)
        two = Succ(one)
        three = Succ(two)
        # self.assertEqual(zero, zero - one)
        # self.assertEqual(zero, zero.subtract(one))
        # self.assertEqual(one, three - two)
        self.assertEqual(one, three.subtract(two))
        # self.assertEqual(three, three - zero)
        # self.assertEqual(three, three.subtract(zero))

    def test_multiply(self):
        zero = Zero()
        two = Succ(Succ(zero))
        three = Succ(two)
        six = Succ(Succ(Succ(three)))
        # self.assertEqual(zero, zero * six)
        # self.assertEqual(zero, zero.multiply(six))
        # self.assertEqual(zero, six * zero)
        # self.assertEqual(zero, six.multiply(zero))
        # self.assertEqual(six, three * two)
        self.assertEqual(six, three.multiply(two))

    # def test_less_than(self):
    #     zero = Zero()
    #     two = Succ(Succ(zero))
    #     three = Succ(two)
    #     self.assertLess(zero, three)
    #     self.assertTrue(zero.less_than(three))
    #     self.assertLess(two, three)
    #     self.assertTrue(two.less_than(three))
