"""Unit testing for dictionary functions."""


__author__ = "730577220"


from dictionary import invert, favorite_color, count

# Edge case test for invert function
def test_invert_empty() -> None:
    """Inverting an empty dictionary."""
    assert invert({}) == {}


# Use case for invert function
def test_invert_regular() -> None:
    """"Inverting a dictionary."""
    assert invert({"Ava": "Joe", "Mia": "Nick"}) == {"Joe": "Ava", "Nick": "Mia"}


# Edge case for favorite color function 
def test_favorite_color_empty() -> None:
    """Testing an empty dictionary."""
    assert favorite_color({}) == ""


# Use case for favorite color function 
def test_favorite_color_repeats() -> None:
    """Testing a dictionary with repeated favorite colors."""
    assert favorite_color({"Ava": "blue", "Nick": "red", "Josh": "blue"}) == "blue"


# Use case for favorite color function 
def test_favorite_color_unique() -> None:
    """Testing a dictionary with all different favorite colors."""
    assert favorite_color({"Ava": "blue", "Nick": "red", "Josh": "green"}) == "blue"


# Edge case for count function 
def test_count_empty() -> None:
    """Testing an empty list."""
    assert count([]) == {}


# Use case for count function 
def test_count_all_ones() -> None:
    """Testing a list with all unique values."""
    assert count(["yes", "no", "maybe"]) == {"yes": 1, "no": 1, "maybe": 1}


# Use case for count function 
def test_count_repeats() -> None:
    """Testing a list with repeated values."""
    assert count(["yes", "yes", "maybe", "no", "maybe"]) == {"yes": 2, "maybe": 2, "no": 1}

