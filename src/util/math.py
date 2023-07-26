from math import floor

def carpet(n: float, d: int) -> float:
    m = 10 ** d
    return floor(n * m) / m