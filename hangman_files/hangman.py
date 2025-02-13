import random

# This function introduces you to the game 
def greeting():
    print("Welcome to Hangman!")
    name = input("What is your name? ").capitalize()
    print(f"Hello {name}! The game will begin in...\n3...\n2...\n1...")
    # print(f"\nHello {name}. You have {7-guesses} guesses left.\n")

    return name

# This function picks the word from the list of words.txt
def pick_word():
    with open("hangman_files/words.txt", "r") as file: 
        allText = file.read() 
        words = list(map(str, allText.split())) 
        word = random.choice(words)
    # '''This only reads the first line''' ------> word = random.choice(open("hangman_files/words.txt","r").readline().split())
    # '''This is a shorter way of doing with open''' ------> word = random.choice(open("hangman_files/words.txt").read().split())
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

    print(f"This is your word {display}\nYou have {7-guesses} left.")
    print(word)

    while guesses <= 7:
        guess = input("Please guess a letter: ").lower()
        
        for letter in word:
            if guess == letter:
                display = word.replace("_", guess)
                print(display)
            elif guess != letter and guess not in word:
                guesses += 1
                print(f"Oops {name}! You guessed wrong. You have {7-guesses} left.")
                print(display)

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

