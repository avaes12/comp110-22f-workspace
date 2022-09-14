"""EX03 - Worldle - 6 guesses to the secret word."""

__author__ = "730577220"


def contains_char (start: str, single: str) -> bool :
    """Checks if single is contained in start"""
    assert len(single) == 1
    # Loops through string of any length to find occurence of single character string
    i: int = 0
    while i < len(start):
        if single[0] == start[i]:
            return True
        i += 1
    return False


def emojified (guess: str, secret: str) -> str:
    """Returns emoji string whose color code matches EX02."""
    assert len(guess) == len(secret)
   
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    # Created an indexing variable and empty string variable that will store emojis
    result: str = ""
    i: int = 0
    while i < len(guess):
    # Returning true - character is in secret word
        if contains_char(secret, guess[i]):
        # Nested if statement to discern difference between green/yellow
            if secret[i] == guess[i]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
    # Returning false - character is not in secret word
        else:
            result += WHITE_BOX
        i += 1
    return(result)


def input_guess(a: int) -> str:
    """Prompts the user for a guess of expected length"""
    beginning: str = input(f"Enter a {a} character word: ")
# Loop will prompt user until the guess is the correct length
    while len(beginning) != a:
    # f string will input the expected length into the display message 
        beginning = input(f"That wasn't {a} chars! Try again: ")
    return(beginning)  


def main() -> None:
    """The entrypoint of the program and main game loop."""
 # Keeping track of secret word, the user's current turn, whether the user has won or not
    secret_word: str = "codes"
    current_turn: int = 1
    win_or_lose: bool = False
# Loops while the user has 6 turns or less and has not won
    while (current_turn < 7) and not (win_or_lose):
        print(f"=== Turn {current_turn}/6 === ")
        first_guess: str = input_guess(len(secret_word))
        first_result: str = emojified(first_guess, secret_word)
    # Stores and prints resulting emoji string
        print(first_result)
    # The loop will stop iterating if the user has won 
        if first_guess == secret_word:
            win_or_lose = True
        current_turn += 1
# Final display messages
    if win_or_lose:
        print(f"You won in {current_turn - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()