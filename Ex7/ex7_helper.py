def add(x: float, y: float) -> float:
    return x + y


def subtract_1(x: int) -> int:
    return x - 1


def is_odd(n: int) -> bool:
    return n % 2 == 1


def divide_by_2(n: int) -> int:
    return n // 2


def append_to_end(s: str, c: str) -> str:
    assert len(c) == 1

    return s + c

