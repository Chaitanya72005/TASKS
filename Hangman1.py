import random

# List of words for the game
words = ['python', 'java', 'javascript', 'html', 'css']

# Select a random word from the list
word = random.choice(words)

# Create an empty list to hold the guessed letters
guessed_letters = []

# Set the number of tries the player has
tries = 6

# Loop until the player has no more tries
while tries > 0:

    # Create a string to hold the letters that have been guessed correctly
    guessed_word = ""
    for letter in word:
        if letter in guessed_letters:
            guessed_word += letter
        else:
            guessed_word += "_"

    # Print the current state of the game
    print("Word: " + guessed_word)
    print("Tries left: " + str(tries))

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # If the player has already guessed the letter, ask them to guess again
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # If the guess is correct, let the player know and check if they have won
    if guess in word:
        print("Correct!")
        if "_" not in guessed_word:
            print("You win!")
            break
    # If the guess is incorrect, let the player know and decrement their tries
    else:
        print("Incorrect.")
        tries -= 1

# If the player has no more tries, let them know they have lost
if tries == 0:
    print("You lose. The word was " + word + ".")
