import random

from src.arithmetic.nat import Nat
from src.arithmetic.succ import Succ
from src.arithmetic.zero import Zero

class NatGenerator():

    def __init__(self: 'NatGenerator') -> 'NatGenerator':
        config_size: int = 0

    def configure(self: 'NatGenerator', size: int) -> None:
        if size >= 0:
            self.config_size: int = size
        else:
            self.config_size: int = 0

    def generate(self: 'NatGenerator') -> Nat:
        if self.config_size <= 0:
            retval: Zero = Zero()
        else:
            size: int = random.randint(0, self.config_size)
            retval: Nat = Zero()
            i: int = 0
            while i < size:
                retval: Succ = Succ(retval)
                i += 1
        return retval
