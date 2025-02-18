import random

# This function introduces you to the game 
def greeting():
    global name
    print("Welcome to Hangman!")
    name = input("What is your name? ").capitalize()
    # print(f"\nHello {name}. You have {7-guesses} guesses left.\n")

    return name

# This function picks the word from the list of words.txt
def pick_word():

    while True:
        choose = input("\nWould you like to be randomly given a word or would you like to select your word?\nType 1 for random and 2 for select: ")
        try:
            choose = int(choose)
            if choose == 1:
                with open("hangman_files/words.txt", "r") as file: 
                    allText = file.read() 
                    words = list(map(str, allText.split())) 
                    word = random.choice(words)
                    break
                    return word
                    # '''This only reads the first line''' ------> word = random.choice(open("hangman_files/words.txt","r").readline().split())
                    # '''This is a shorter way of doing with open''' ------> word = random.choice(open("hangman_files/words.txt").read().split())
            elif choose == 2:
                word = input("\nPlease enter your word: ").lower().strip()
                if not word.isalpha():
                    print(f"You have entered {word}. Please enter a valid word.")
                else:
                    break
                    return word
            else:
                print("\nInvalid input: please try again")
        except ValueError:
            print("\nInvalid input: cannot convert to integer") 
    return word

def run_game(): 
    global display   
    global guesses
    guesses = 0
    name = greeting()
    word = pick_word()
    display = ""
    for i in range(0,len(word)):
        display += "_"
    
    print(f"\nHello {name}! The game will begin in...\n3...\n2...\n1...\n")
    print(f"This is your word {display}\nYou have {7-guesses} guesses left.\n")
    print(word)
    display_list = list(display)
    word_list = list(word)

    while guesses < 7:
        guess = input("Please guess a letter: ").lower().strip()
        if guess.isalpha():

                # if guess == letter:
                #     index = word.index(letter)
                #     string_list[index] = guess
                #     display = "".join(string_list)
            # In [1]: mystring = "whatever"

            # In [2]: mystring.replace('er', 'u')
            # Out[2]: 'whatevu'
            if guess in word:
                for letter in word:
                    # b = map(lambda x: x + 4 if x < 0 else x, a)
                    display_list = map(lambda guess: "_" if letter != guess else letter for letter in word)
                    # display_list = ["_" if letter != guess else letter for letter in word]
                    display = "".join(display_list)
                print(display)

                # for letters in word:
                #     index = word_list.index(letters,0,len(word_list))
                #     string_list[index] = guess
                #     display = "".join(string_list)
        else:
            print(f"You have entered: {guess}. Please enter a valid guess.\n")

# This function handles if you've lost the game
def lost():
    pass

# This function handles if you've won the game
def won():
    pass

# This function tells us if you've won of lost the game
def outcome():
    pass

if __name__ == "__main__":
    run_game()

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

