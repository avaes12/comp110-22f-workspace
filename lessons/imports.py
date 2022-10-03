"""Examples of importing Python."""


from lessons import helpers
from lessons import helpers as hp
# import function directly 
from lessons.helpers import powerful

def main() -> None:
    """Entrypoint of program."""
    print(hp.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")

if __name__ == "__main__" :
    main()
