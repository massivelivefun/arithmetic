from .nat import Nat

class Zero(Nat):
    def __init__(self: 'Zero') -> 'Zero':
        pass

    def is_zero(self: 'Zero') -> bool:
        return True

    def is_one(self: 'Zero') -> bool:
        return False

    def add(self, other: Nat) -> Nat:
        return other

    def __add__(self, other: Nat) -> Nat:
        return other

    def subtract(self, other: Nat) -> Nat:
        return self

    def __sub__(self, other: Nat) -> Nat:
        return self

    def multiply(self, other: Nat) -> Nat:
        return self

    def __mul__(self, other: Nat) -> Nat:
        return self

    def equals(self, other: Nat) -> bool:
        return isinstance(other, Zero)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Zero)

    def __repr__(self) -> str:
        return '0'

    def __str__(self) -> str:
        return '0'

    def less_than(self, other: Nat) -> bool:
        return not other.is_zero()

    def __lt__(self, other: Nat) -> bool:
        return not other.is_zero()
