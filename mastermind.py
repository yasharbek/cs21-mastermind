"""

The program generates a secret "code", which is a list of four
colors e.g. "green green blue red".
There are six possible colors: red, yellow, blue, green, orange, and purple.

The game ends if the user guesses all 4 colors in their exact positions
in 10 tries or if the user runs out of tries. Each turn,
the player enters a guess for the code e.g. "blue orange yellow blue".
The computer then reports how many exact matches the player had, and
how many inexact matches the player had.

An inexact match is when the player guesses the color correctly,
but not the position, and an exact match is
when the player guesses a color correctly
and puts it in the correct position.

Yasharbek Sabitov CS21
2021-10-07
"""


def print_introduction():
    """
    Just some basic instructions
    """

    print()
    print()
    print("Welcome to Mastermind!\n"
    "\nYour goal is to guess a sequence of four colors"
    "\nYour guess should be out of blue, green, red, orange, purple, or yellow."
    "\n\nAfter your guess, the program will tell you"
    " how many times \nyou guessed the correct color"
    "in the correct position, and how \nmany times you guessed the"
    "correct color, \nbut in the wrong position."
    " You have ten attempts \nto guess the correct sequence."
    "\n\nYou can also type 'quit' or 'exit' to close the program.")

def is_game_over(num_exact_matches, turn):
    """
    Tests if the game should end. This is a boolean function
    """
    if num_exact_matches == 4 or turn == 9:
        return True
    else:
        return False

def print_colors(color_list):
    """

    List of appropriate colors to input
    so the user knows not to randomly input stuff

    Yashar CS21
    """

    newlist = ["red", "orange", "yellow", "green", "blue", "purple"]
    color_list = newlist
    print("Please enter four legal colors. Your choices are: ")
    length = len(color_list)
    stringaccum = ""
    for colors in range(length):
        diff = length - colors
        if diff > 1:
            stringaccum = stringaccum + color_list[colors] + ", "
        else:
            stringaccum = stringaccum + color_list[colors] + "."
    print(stringaccum)
    return color_list

def get_guess(colors):
    """
    Collects guesses, adds them to a list and prints em out for the
    user to see their own input
    """

    newlist = ["red", "orange", "yellow", "green", "blue", "purple"]
    collectionlist = []
    colors = input("Enter color 1: ")
    if colors == "exit" or "quit":
        quit()
    else:
        for i in range(1,5):
            while colors not in newlist:
                print("%s is not a valid color." % colors)
                print_colors(newlist)
                colors = input("Enter color %d: "% i)
            collectionlist.append(colors)
            if (i+1) < 5:
                colors = input("Enter color %d: " % (i+1))
        print("You guessed: " + collectionlist[0] + ", " + collectionlist[1] + ", "
        + collectionlist[2] + ", " + collectionlist[3] + ".")
        return collectionlist

def generate_code(colors):
    """
    Randomly generates a secret code
    """

    from random import choice
    samplecolors = ["red", "orange", "yellow", "green", "blue", "purple"]
    truecolors = []
    for i in range(1,5):
        truecolors.append(choice(samplecolors))
    return truecolors

def exact_matches(secret_code, guess, status):
    """

    calculates the number of exact matches in a guess and returns an integer
    that is later used to keep track of winner's exact matches. vibes

    """

    number = 0
    for i in range(4):
        if secret_code[i] == guess[i] and status[i] != "exact":
            status[i] = "exact"
            number += 1

    return number

def inexact_matches(secret_code, guess, status):
    """
    Keeps track of the user's inexact matches in a guess

    """

    number = 0
    for i in range(4):
        if status[i] != "exact":
            for ind in range(4):
                if guess[i] == secret_code[ind] and status[ind] == "":
                    status[ind] = "inexact"
                    number += 1
    return number

def player_won(num_exact_matches):
    """
    A function that's later used to test whether
    the game should end
    """
    if num_exact_matches == 4:
        return True
    else:
        return False

def main():
    """
    This function keeps track (but doesn't print) of overall exact matches
    guessed as opposed to individual guess rounds. Also tests if the game
    should end.
    """
    print_introduction()
    list = []
    secretcode = generate_code(list)
    choicecol = ""
    status = ["", "", "", ""]
    print()
    exactlyaccum = 0
    for i in range(10):
        print()
        print()
        if exactlyaccum != 4:
            print("Round %d:" % (i+1))
            listic = print_colors(list)
            userscode = get_guess(choicecol)
            exactly = exact_matches(secretcode, userscode, status)
            exactlyaccum += exactly
            inexactly = inexact_matches(secretcode, userscode, status)
            print("# of exact matches u found this round: " + str(exactly) +
            "\n" "# of inexact matches u found this round: " + str(inexactly))
            gameoveror = is_game_over(exactlyaccum, i)
            print()
            print()
            if gameoveror == True:
                break
    wonor = player_won(exactlyaccum)
    if wonor == True:
        print("Congrats! You won")
        print("It took you %d turns to get the correct answer!" % (i+1))
    else:
        print("You lost :()")
    print("The correct answer was: " + secretcode[0] + ", "
    + secretcode[1] + ", " + secretcode[2] +
    ", " + secretcode[3] + ".")
main()
