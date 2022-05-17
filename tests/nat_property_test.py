from pathlib import Path

relative_path_to_project_root = \
    Path(__file__).resolve().parent.parent

import sys
sys.path.append(str(relative_path_to_project_root))

import unittest

from src.arithmetic.nat import Nat
from src.arithmetic.succ import Succ
from src.arithmetic.zero import Zero

from tests.nat_generator import NatGenerator

from hypothesis import given, example
from hypothesis.strategies import integers

class NatPropertiesTest(unittest.TestCase):
    @given(integers(min_value=0, max_value=10))
    def test_number_equals_self(self, num):
        gen: NatGenerator = NatGenerator()
        gen.configure(num)
        peano_num: Nat = gen.generate()
        self.assertEqual(peano_num, peano_num)
        self.assertTrue(peano_num == peano_num)

    @given(integers(min_value=0, max_value=10))
    def test_addition(self, num):
        gen: NatGenerator = NatGenerator()
        gen.configure(num)
        peano_num: Nat = gen.generate()
        self.assertEqual( peano_num.add(Zero()), peano_num )
        self.assertEqual( Zero().add(peano_num), peano_num )
        self.assertEqual( peano_num + Zero(), peano_num)
        self.assertEqual( Zero() + peano_num, peano_num)

    @given(integers(min_value=0, max_value=10))
    def test_subtraction(self, num):
        gen: NatGenerator = NatGenerator()
        gen.configure(num)
        peano_num: Nat = gen.generate()
        next_peano_num = Succ(peano_num)
        self.assertEqual( peano_num.subtract(Zero()), peano_num )
        self.assertEqual( Zero().subtract(peano_num), Zero() )
        self.assertEqual( peano_num.subtract(next_peano_num),
                        Zero() )
        self.assertEqual( peano_num - Zero(), peano_num)
        self.assertEqual( Zero() - peano_num, Zero())
        self.assertEqual( peano_num - next_peano_num,
                        Zero() )

    @given(integers(min_value=0, max_value=10))
    def test_multiplication(self, num):
        gen: NatGenerator = NatGenerator()
        gen.configure(num)
        peano_num: Nat = gen.generate()
        next_peano_num = Succ(peano_num)
        self.assertEqual( peano_num.multiply(Zero()), Zero() )
        self.assertEqual( Zero().multiply(peano_num), Zero() )
        self.assertEqual( peano_num.multiply(next_peano_num),
                        next_peano_num.multiply(peano_num) )
        self.assertEqual( peano_num * Zero(), Zero())
        self.assertEqual( Zero() * peano_num, Zero())
        self.assertEqual( peano_num * next_peano_num,
                        next_peano_num * peano_num)

    @given(integers(min_value=1, max_value=10))
    def test_less_than(self, num):
        gen: NatGenerator = NatGenerator()
        gen.configure(num)
        peano_num: Nat = gen.generate()
        next_peano_num = Succ(peano_num)
        self.assertLess(Zero(), peano_num)
        self.assertLess(Zero(), next_peano_num)
        self.assertTrue( Zero().less_than(peano_num) )
        self.assertTrue( peano_num.less_than(next_peano_num) )
        self.assertTrue( Zero() < peano_num)
        self.assertTrue( peano_num < next_peano_num)

    @given(integers(min_value=0, max_value=10))
    def test_equals_operator(self, num):
        gen: NatGenerator = NatGenerator()
        gen.configure(num)
        peano_num: Nat = gen.generate()
        next_peano_num = Succ(peano_num)
        self.assertTrue(peano_num.equals(peano_num))
        self.assertTrue(next_peano_num.equals(next_peano_num))
        self.assertFalse(peano_num.equals(next_peano_num))
        self.assertFalse(next_peano_num.equals(peano_num))
        self.assertFalse(peano_num.equals(object()))
        self.assertFalse(next_peano_num.equals(object()))
        self.assertTrue(peano_num == peano_num)
        self.assertTrue(next_peano_num == next_peano_num)
        self.assertFalse(peano_num == next_peano_num)
        self.assertFalse(next_peano_num == peano_num)
        self.assertFalse(peano_num == next_peano_num)
        self.assertFalse(next_peano_num == peano_num)
        self.assertFalse(peano_num == object())
        self.assertFalse(next_peano_num == object())

if __name__ == "__main__":
    unittest.main()
