from decimal import Decimal
from typing import TypeVar, Protocol

T = TypeVar('T')

pi = Decimal(22) / Decimal(7)

class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...

RT = TypeVar('RT', bound=Repeatable)

def double(x: RT) -> RT:
    return x * 2

print(f"{double(4) = }")
print(f"{double('D') = }")
print(f"{double([1, 2, 3, 4]) = }")
print(f"{double(pi) = }")
print(f"{double((1, 2, 3)) = }")
print(f"{double({1:1, 2:2}) = }")
