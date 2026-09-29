import random

# Predefined words
words = ["python", "computer", "programming", "keyboard", "internet"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Game settings
incorrect_guesses = 0
max_incorrect_guesses = 6

# Hangman drawing stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


print("================================")
print("          HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses available.\n")


while incorrect_guesses < max_incorrect_guesses:

    # Display Hangman drawing
    print(hangman_stages[incorrect_guesses])

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:",
          incorrect_guesses, "/", max_incorrect_guesses)

    # Check if the player has guessed the whole word
    if "_" not in display_word:
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Incorrect guess!\n")


# Losing condition
if incorrect_guesses == max_incorrect_guesses:
    print(hangman_stages[incorrect_guesses])
    print("Game Over!")
    print("The correct word was:", word)