import random

yes = "Y"
no = "N"
exit_game = "E"

def intro():
    print("\nWelcome to a game of Rock, Paper or Scissors!")
    name = input("What is your name? ").capitalize()

    print(f"\nHi {name}!\nThe rules are as follows.")
    print("1. Enter R for rock, P for paper and S for scissors")
    print("2. There are 3 rounds. Best out of 3 wins!")
    print("3. Enter E to exit the game")

    print("Let the games begin!\n")
    game()

def game():
    rock = "R"
    paper = "P"
    scissors = "S"
    computer = "C"

    player_points = 0
    computer_points = 0
    rounds = 0

    while rounds < 3:
        player_choice = input(f"This is round {rounds + 1}\nRock, paper or scissor? ").upper()
        computer_options = [rock, paper, scissors]
        computer_choice = random.choice(computer_options) 

        if player_choice == rock or player_choice == paper or player_choice == scissors or player_choice == exit_game:
            pass
            # Player loses
            if player_choice == rock and computer_choice == paper:
                computer_points += 1
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You lost and did not gain a point!\n")
            elif player_choice == paper and computer_choice == scissors:
                computer_points += 1
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You lost and did not gain a point!\n")
            elif player_choice == scissors and computer_choice == rock:
                computer_points += 1
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You lost and did not gain a point!\n")
            
            # Player wins
            elif player_choice == paper and computer_choice == rock:
                player_points += 1
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You won and gained a point!\n")
            elif player_choice == scissors and computer_choice == paper:
                player_points += 1
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You won and gained a point!\n")
            elif player_choice == rock and computer_choice == scissors:
                player_points += 1
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You won and gained a point!\n")

            # Draw
            elif player_choice == computer_choice:
                rounds += 1
                print(f"Your choice: {player_choice}")
                print(f"Computer choice: {computer_choice}")
                print("You both picked the same option!\n")
            
            # Exit game
            elif player_choice == exit_game:
                quitting = input("\nYou are about to exit the game. Are you sure? Y or N: ").upper()
                if quitting == yes:
                    quit
                    break
                    quit_game()
                else:
                    print("The game will restart now...\n")
                    intro()

        else:
            print("You have put an invalid answer. The game will restart...\n")
            game()

    if rounds == 3 and player_points > computer_points:
        print("You win the game!\n")
        play_again()
    elif rounds == 3 and computer_points > player_points:
        print("You lost the game!\n")
        play_again()
    elif rounds == 3 and player_points == computer_points:
        print("It's a draw!\n")
        play_again()
    elif rounds < 3 and player_choice == exit_game:
        quit_game()
    else:
        print("The game has ended but no one has won...")
        play_again()

def play_again():
    question = input("Would you like to play again? Y or N: ").upper()
    if question == yes:
        intro()
    elif question == no:
        quit
    else:
        play_again()

def quit_game():
    print("\nGoodbye!")
    quit

if __name__ == "__main__":
    intro()

# Modifications 

# Checks for correct inputs
# Change name/player on next game