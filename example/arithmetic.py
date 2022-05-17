from pathlib import Path

relative_path_to_project_root = \
    Path(__file__).resolve().parent.parent

import sys
sys.path.append(str(relative_path_to_project_root))

from src.arithmetic.nat import Nat
from src.arithmetic.succ import Succ
from src.arithmetic.zero import Zero

if __name__ == "__main__":

    three = Succ(Succ(Succ(Zero())))
    two = Succ(Succ(Zero()))

    five = three.add(two)
    six = three.multiply(two)
    four = two.add(two)

    one = three - two
    seven = (three * two) + one
    eight = four * two
    nine = three * three

    zero = Zero()

    if three == three:
        print('Three is equal to three!')

    if four < nine:
        print('Four is less than nine!')

    if five.equals(five):
        print('Five is equal to five!')

    if zero.is_zero():
        print('Zero is zero!')

    if one.is_one():
        print('One is one!')

    print('nine:\t' + str(nine))
    print('eight:\t' + str(eight))
    print('seven:\t' + str(seven))
    print('six:\t' + str(six))
    print('five:\t' + str(five))
    print('four:\t' + str(four))
    print('three:\t' + str(three))
    print('two:\t' + str(two))
    print('one:\t' + str(one))
    print('zero:\t' + str(zero))
