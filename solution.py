"""
Kyle Kekawa, Bryan Mai 8/30/2023 This is our second lab assignment which is a random card generator along with 
a betting mechanism. If you run out of money you LOSE! 

"""

import random

"""
This is a function, that takes input of the users bet if it is not a number it prints outs a invalid output
"""
def get_users_bet(money):
    print(f"You have ${money}")
    while True: 
        try:
            bet = int(input("How much you wanna bet?"))
            if 1 <= bet <= money:
             return bet
            else:
             print("Invalid input - should be within 1-" + str(money) + ".")
        except ValueError: 
            print("Invalid input - should be an integer.")


"""
Displays the 3 cards across the "board" and allows the user to select their choice
"""
def get_users_choice():
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")
    while True:
            try: 
                choice = int(input("Find the queen: ")) 
                if 1 <= choice <= 3:
                    return choice
                else: 
                    print("Invalid input - Should be a number between 1 and 3")
            except ValueError: 
                print("Invalid input - should be an integer.")
        



def display_queen_loc(queen_loc: int) -> None:
    """
    This is the function where it calls the Queen card or is created. 
    """
    cards = ["K", "K", "K"]
    cards[queen_loc - 1] = "Q"
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  " + cards[0] + "  | |  " + cards[1] + "  | |  " + cards[2] + "  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")
    


def main():
    print("-Three card Monte-")
    print("Find the queen to double your bet!")

    money = 100
    play_again = True

    while play_again and money > 0: 
        queen_location = random.randint(1, 3) #The random generator switches the queen card between 1 - 3    

        bet = get_users_bet(money) #Calls the functions of both the user's bet and user's choice with the code below 
        choice = get_users_choice()

        display_queen_loc(queen_location)

        if choice == queen_location: #Picking a number from 1 - 3 to see if you make the correct selection. 
            print("You got lucky this time...") 
            money += bet 
        else:
            print("Sorry... you lose.")
            money -= bet

        print("You have $" + str(money) + ".") #Printing the remainder of your money (gambling's bad)

        play_again_input = input("Play again? (Y/N): ") #Asking if you wanna play again but you should probably walk away
        play_again = play_again_input.lower() == "y"    #Walk away when winning 

    if money <= 0:
        print("You're out of money. Beat it loser!")

if __name__ == "__main__":
    main()