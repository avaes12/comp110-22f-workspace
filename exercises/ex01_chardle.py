"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730577220"

start: str = input("Enter a 5 character word: ")
root: str = input("Enter a single character: ")
count: int = 0

if(len(start)!= 5) :
    print("Word must contain 5 characters")
    exit()
if(len(root) != 1) :
    print("Character must be a single character.")
    exit()

print("Searching for " + root + " in " + start)

if(start[0]== root) :
    print(root + " found at index 0")
    count = count + 1
if(start[1] == root) :
    print(root + " found at index 1")
    count = count + 1
if(start[2] == root) :
    print(root + " found at index 2")
    count = count + 1
if(start[3]==root) :
    print(root + " found at index 3")
    count = count + 1
if(start[4] == root) :
    print(root + " found at index 4")
    count = count + 1


if(count == 0) : 
    print("No instances of " + root + " found in " + start)
if(count == 1) :
    print("1 instance of " + root + " found in " + start)
if(count>1) :
    print(str(count) + " instances of " + root + " found in " + start)                    
    