from .nat import Nat

class Succ(Nat):
    def __init__(self: 'Succ', around: Nat) -> 'Succ':
        self.around: Nat = around

    def is_zero(self) -> bool:
        return False

    def is_one(self) -> bool:
        return self.around.is_zero()

    def add(self, other: Nat) -> Nat:
        retval: Nat = other
        cur: Nat = self
        while not cur.is_zero():
            retval: Succ = Succ(retval)
            cur: Succ = cur.around
        return retval

    def __add__(self, other: Nat) -> Nat:
        retval: Nat = other
        cur: Nat = self
        while not cur.is_zero():
            retval: Succ = Succ(retval)
            cur: Succ = cur.around
        return retval

    def subtract(self, other: Nat) -> Nat:
        if other.is_zero():
            return self
        else:
            otherSucc: Succ = other
            return self.around.subtract(otherSucc.around)

    def __sub__(self, other: Nat) -> Nat:
        if other.is_zero():
            return self
        else:
            otherSucc: Succ = other
            return self.around.subtract(otherSucc.around)

    def multiply(self, other: Nat) -> Nat:
        if other.is_zero():
            return other
        else:
            cur: Nat = other
            retval: Nat = self
            while not cur.is_one():
                retval: Succ = retval.add(self)
                cur: Succ = cur.around
            return retval

    def __mul__(self, other: Nat) -> Nat:
        if other.is_zero():
            return other
        else:
            cur: Nat = other
            retval: Nat = self
            while not cur.is_one():
                retval: Succ = retval + self
                cur: Succ = cur.around
            return retval

    def equals(self, other: object) -> Nat:
        if isinstance(other, Nat):
            cur: Nat = self
            otherNat: Nat = other
            while not cur.is_zero() and not otherNat.is_zero():
                cur: Succ = cur.around
                otherNat: Succ = otherNat.around
            return cur.is_zero() and otherNat.is_zero()
        else:
            return False

    def __eq__(self, other: object) -> Nat:
        if isinstance(other, Nat):
            cur: Nat = self
            otherNat: Nat = other
            while not cur.is_zero() and not otherNat.is_zero():
                cur: Succ = cur.around
                otherNat: Succ = otherNat.around
            return cur.is_zero() and otherNat.is_zero()
        else:
            return False

    def __repr__(self) -> str:
        numRightParens: int = 0
        buffer: str = ''
        cur: Nat = self
        while not cur.is_zero():
            buffer += 'S('
            cur: Succ = cur.around
            numRightParens = numRightParens + 1
        buffer += '0'
        for _ in range(0, numRightParens):
            buffer += ')'
        return buffer

    def __str__(self) -> str:
        numRightParens: int = 0
        buffer: str = ''
        cur: Nat = self
        while not cur.is_zero():
            buffer += 'S('
            cur: Succ = cur.around
            numRightParens = numRightParens + 1
        buffer += '0'
        for _ in range(0, numRightParens):
            buffer += ')'
        return buffer

    def less_than(self, other: Nat) -> bool:
        cur: Nat = self
        while not cur.is_zero() and not other.is_zero():
            cur: Succ = cur.around
            other: Succ = other.around
        return cur.is_zero() and not other.is_zero()

    def __lt__(self, other: Nat) -> bool:
        cur: Nat = self
        while not cur.is_zero() and not other.is_zero():
            cur: Succ = cur.around
            other: Succ = other.around
        return cur.is_zero() and not other.is_zero()
