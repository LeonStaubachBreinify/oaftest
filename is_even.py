"""
Function that returns whether a given number or odd.
"""
def is_even(number: int) -> bool:
    return number % 2 == 0

def is_odd(number: int) -> bool:
    return not is_even(number)