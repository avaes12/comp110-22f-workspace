"""Practicing with dictionary functions."""


__author__ = "730577220"


import numbers
from sys import builtin_module_names


def invert(blocks: dict[str, str]) -> dict[str, str]:
    """Inverting a dictionary, keys become values, values become keys."""
    
    # Establish an empty dictionary to store inverted keys and values
    logs: dict[str, str] = {}

    # Looping through given dictionary
    for key in blocks:
        
        # Establish boolean to check for existence of key
        possible_duplicate: bool = key in logs
        logs[blocks[key]] = key
        
        # Key error raised if the given dictionary two or more of the same values
        if possible_duplicate:
            raise KeyError("Keys were found to be the same.")
    
    return logs


def favorite_color(rainbows: dict[str, str]) -> str:
    """Returning the most common favorite color from a dictionary."""
    
    # Establishing an empty dictionary, key is color, value is # of occurences
    color_count: dict[str, int] = {}

    # Looping through given dictionary 
    for name in rainbows:
        
        # Each key in the new dictionar will be a color 
        color: str = rainbows[name] 

        # Establishing a boolean to check for duplicate favorite colors
        color_present: bool = color in color_count
        
        if color_present:
            # Increments color count if the color is already present in new dictionary
            color_count[color] += 1
        else:
            # Establishes color count as 1 if the color is not already present in dictionary
            color_count[color] = 1


    # Established an int to keep track of the highest value in colors dictioary
    highest_tally: int = 0

    # Established a str that will represent the most popular favorite color 
    highest_color: str = ''

    # Looping through color dictionary 
    for color in color_count:
        
        # The values of the color dictionary are the # of occurences of color in given dictionary
        tally: int = color_count[color]
        
        # Compares values of the dictionary to find the greatest value
        if tally > highest_tally:
            highest_tally = tally
            highest_color = color      
     
    return highest_color
        

def count(log: list[str]) -> dict[str, int]:
    """Each value in the list has a value of how many times it occured in the list."""
   
    # Establish a new dictionary to return 
    blocks: dict[str, int] = {}
   
    # Count variable to keep track of list indices 
    i: int = 0

    # Looping through given list 
    while i < len(log):

        if log[i] in blocks:
            # Increments value if the list item is already present in new dictionary
            blocks[log[i]] += 1
        else:
            # Sets value at 1 if list item is not already present in new dictionary 
            blocks[log[i]] = 1
        i += 1
    return blocks
