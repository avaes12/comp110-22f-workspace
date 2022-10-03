"""Choose your own adventure project. Sandwich Shop!"""


__author__ = "730577220"


from random import randint


# global variables
points: int = 0
player: str = ""


# global named constants for emojis 
HAPPY_FACE: str = "\U0001F600"
SANDWICH: str = "\U0001F96A"
COOKIE: str = "\U0001F36A"
HAND_WAVE: str = "\U0001F44B"


# greet procedure
def greet() -> None:
    """Opening message to the game."""
    global player 
    player = input("What is your name?: ")
    print(f"Welcome to Sandwich Shop {player}! {HAND_WAVE}{HAPPY_FACE}")


# sandwich artist is the game procedure 
# one option of the main function 
def sandwich_artist() -> None:
    """Building the sandwich."""
   # points will refer to the global variable
    global points

    # asks the player for an integer to determine bread
    bread: str = input("0 or 1?: ")
    if bread == "1":
        bread = "white"
        points += 1
    else:
        bread = "wheat" 
        points += 2
    
    # asks the player for an integer to determine meat 
    meat: str = input("0, 1, or 2? : ")
    if meat == "2":
        meat = "salami"
        points += 1
    elif meat == "1":
        meat = "ham"
        points += 2
    else:
        meat = "turkey"
        points += 3

    # asks the player for an integer to determine cheese 
    cheese: str = input("0, 1, or 2?: ")
    if cheese == "2":
        cheese = "american"
        points += 3
    elif cheese == "1":
        cheese = "cheddar"
        points += 2
    else:
        cheese = "mozzerella"
        points += 1

    # every sandwich automatically gets lettuce and pickles
    veggies: list[str] = ["lettuce", "pickles"]
    extras: str = input("0, 1, or 2?: ")
    # asks player for an integer to determine the additional veggie 
    if extras == "2": 
        veggies.append("spinach")
        points += 3
    elif extras == "1":
        veggies.append("cucumbers")
        points += 2
    else:
        veggies.append("tomatoes")
        points += 1

    # final order is printed 
    print(f"Here is your sandwich with {meat}, {cheese}, and {veggies} on {bread}. {SANDWICH}")

# bonus round determines prize and/or discount 
def bonus_round(bonus_score: int) -> int: 
    """Alters the total price variable."""
    if bonus_score < 7:
        print(f"Yay! You got a cookie and a discount!{HAPPY_FACE}{COOKIE}")
        # the random function is used to determine the discount
        # discount is subtracted from bonus score 
        bonus_score -= randint(0,3)
    return bonus_score


def main() -> None:
    """A fun sandwich game."""

    # greets player 
    greet()

    # variable to track the game loop 
    customer_request: str = input("Would you like a sandwich? Yes or No:  ")

    while customer_request == "Yes":
        # player wants a sandwich, artist/bonus functions called 
        sandwich_artist()
        bonus_round(points)
        # game loop will continue as long as player wants more sandwiches 
        customer_request = input("Any more sandwiches? Yes or No: ")
    
    # Total price is printed (equal to the game points)
    print(f"Your total will be ${points}.")

    # Goodbye message 
    print(f"Have a nice day {player}. Come back soon. {HAND_WAVE}")


if __name__ == "__main__":
    main()
    