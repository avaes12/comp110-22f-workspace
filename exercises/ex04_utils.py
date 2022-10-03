"""Reverse engineering algorithims with lists."""

__author__ = "730577220"


def all(turns: list[int], go: int) -> bool:
    """Returns true if every item in turns matches go."""
    i: int = 0 
    while i < len(turns):
        if turns[i] != go:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest item in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    largest: int = input[0] 
    while i < len(input):
        if input[i] > largest:
            largest = input[i] 
        i += 1
    return largest


def is_equal(trials: list[int], options: list[int]) -> bool:
    """Returns true if every element in both lists is the same at the same indices."""
    if len(trials) != len(options):
        return False
    i: int = 0 
    while i < len(trials):
        if trials[i] != options[i]:
            return False
        i += 1
    return True