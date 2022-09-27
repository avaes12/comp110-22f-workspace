"""Function skeletons."""

__author__ = "730577220"


def only_evens(nums: list [int]) -> list[int]:
    """Returns a new list of only the even elements of nums."""
    i: int = 0
    even_nums: list[int] = []
    # Created a new list and a tracking variable 
    while i < len(nums):
        if nums[i] % 2 == 0:
            #If the element is even, add it to the new list
            even_nums.append(nums[i])
        i += 1
    return even_nums


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns a new list of lists 1 & 2 combined."""
    list_3: list[int] = []
    i: int = 0
    # Created a new list and a tracking variable
    while i < len(list_1):
        # Adding each item of the first list
        list_3.append(list_1[i])
        i += 1
    i = 0
    # Resetting i to 0 to loop through the second list
    while i < len(list_2):
        # Adding each item of the second list 
        list_3.append(list_2[i])
        i += 1
    return list_3

def sub(roster: list[int], i: int, n: int) -> list[int]:
    """"Returns a new list of a specified subset. """
    sub_roster: list[int] = []
    # Creating a new list
    if i < 0:
        # If start index is negative, start at the beginning
        i = 0
    if n > len(roster):
        # If end index is greater than the length, end with the last element
        n = len(roster)
    if (len(roster) == 0) or (i > len(roster)) or (n <= 0):
        # If the length of the list is 0
        # If the start index is greater than the length of the list
        # If the end index is negative, return an empty list
        return []
    while i < n:
        # While the current index is less than the end, add to the list 
        sub_roster.append(roster[i])
        i += 1
    return sub_roster