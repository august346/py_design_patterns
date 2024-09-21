from functools import wraps
from typing import Callable


def func_to_str(i: int) -> str:
    return str(i)


def bin_decorator(func: Callable[[int], str]) -> Callable[[int], str]:
    @wraps(func)
    def wrapper(i: int) -> str:
        bin_i: int = int("{0:b}".format(i))

        return func(bin_i)

    return wrapper
