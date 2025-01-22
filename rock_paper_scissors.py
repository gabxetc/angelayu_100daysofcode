import random

yes = "Y"
no = "N"



def game():
    rock = "R"
    paper = "P"
    scissors = "S"
    computer = "C"

    player_points = 0
    computer_points = 0
    rounds = 0

    print("Welcome to a game of Rock, Paper or Scissors!")
    name = input("What is your name? ").capitalize()

    print(f"Hi {name}!\nThe rules are as follows.")
    print("1. Enter R for rock, P for paper and S for scissors")
    print("2. There are 3 rounds. Best out of 3 wins!")

    print("Let the games begin!\n")

    while rounds < 3:
        player_choice = input("Rock, paper or scissor?").upper()
        computer_options = [rock, paper, scissors]
        computer_choice = random.choice(computer_options)
        print(f"Your choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        
        # Player loses
        if player_choice == rock and computer_choice == paper:
            computer_points += 1
            rounds += 1
            print("You did not gain a point!\n")
        elif player_choice == paper and computer_choice == scissors:
            computer_points += 1
            rounds += 1
            print("You did not gain a point!\n")
        elif player_choice == scissors and computer_choice == rock:
            computer_points += 1
            rounds += 1
            print("You did not gain a point!\n")
        
        # Player wins
        elif player_choice == paper and computer_choice == rock:
            player_points += 1
            rounds += 1
            print("You gained a point!\n")
        elif player_choice == scissors and computer_choice == paper:
            player_points += 1
            rounds += 1
            print("You gained a point!\n")
        elif player_choice == rock and computer_choice == scissors:
            player_points += 1
            rounds += 1
            print("You gained a point!\n")

        # Draw

        elif player_choice == computer_choice:
            rounds += 1
            print("You both picked the same option!\n")
    
    if player_points > computer_points:
        print("You win the game!")
        play_again()
    elif computer_points > player_points:
        print("You lost the game!")
        play_again()
    elif player_points == computer_points:
        print("It's a draw!")
        play_again()

def play_again():
    question = input("Would you like to play again? Y or N: \n").upper()
    if question == yes:
        game()
    elif question == no:
        quit

if __name__ == "__main__":
    game()
