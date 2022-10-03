"""Example implementing a list utility function."""

# Function name contains 
# We will have 2 parameters: needle (str), haystack(list[str])
# True if needle is found in haystack at least once 

def contains(needle: str, haystack: (list[str])) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            #  Found an instance of needle in haystack 
            return True 
        i += 1
    # We tried searching each item and came up short
    return False