"""EX02 - Worldle - User trying to guess secret word"""

__author__ = "730577220"

#variables for secret word/user guess, loop for guesses of incorrect length
secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
while len(guess) != len(secret) :
    guess = input(f"That was not {len(secret)} letters! Try again: ")

#emoji unicodes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#declared counter variable, result string 
i : int = 0
result : str = ""


while i < len(secret):
    #adds a green box if the letters at the same index in guess and secret are the same 
    if guess[i] == secret [i] :
        result += GREEN_BOX    
    else :
        hiding : bool = False 
        a : int = 0
        while (not hiding) and a < len(secret) :
            if secret[a] == guess[i] :
                hiding = True 
            a += 1
        if hiding :
            #adds a yellow box if the letter is in secret but at the incorrect index
            result += YELLOW_BOX
        else :
            #adds a white box if the letter is not in secret 
            result += WHITE_BOX
    i += 1 
#prints resulting string of emojis 
print(result)


