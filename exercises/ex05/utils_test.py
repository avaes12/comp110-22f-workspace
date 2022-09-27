"""Practice writing unit tests for functions."""

__author__ = "730577220"


from utils import only_evens, concat, sub

# Testing an empty list - edge case
def test_only_evens_empty() -> None:
    assert only_evens([]) == []

# Testing a list with only odd numbers - use case
def test_only_evens_odds() -> None:
    assert only_evens([1, 3, 5]) == []

# Testing a list with odd/even numbers - use case
def test_only_evens_mixed() -> None:
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]

# Testing two empty lists - edge case
def test_concat_empty_lists() -> None:
    assert concat([], []) == []

# Testing two lists of the same length - use case
def test_concat_same_lengths() -> None:
    assert concat([1, 2], [1, 2]) == [1, 2, 1, 2]
 
# Testing two lists of different lengths - use case
def test_concat_diff_lengths() -> None:
    assert concat([1, 2], [1, 2, 3]) == [1, 2, 1, 2, 3]

# Testing a list with given start/end indices in range  
def test_sub_in_range() -> None:
    assert sub([1, 2, 3, 4], 1, 2) == [2]

# Testing a list with a given end index greater than length of list 
def test_sub_big_ending() -> None:
    assert sub([1, 2, 3, 4], 1, 5) == [2, 3, 4]

# Testing a list with a given negative start index
def test_sub_low_start() -> None:
    assert sub([1, 2, 3, 4], -1, 2) == [1, 2]

# Testing an empty list, start index greater than length, negative end index
def test_sub_empty() -> None:
    assert sub([], 1, -1) == []