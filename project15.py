# WORD GUESSING GAME
# PROGRAM RULES / FLOW
# 1. Store a collection of words and their hints
#    in a dictionary.
# 2. Randomly select one word from the dictionary.
# 3. Get the hint associated with the selected word.
# 4. Give the player a fixed number of attempts.
# 5. Display the game title and the hint.
# 6. Ask the player to guess the word.
# 7. Convert the guess to lowercase to avoid
#    case-sensitivity issues.
# 8. Check whether the guessed word matches
#    the secret word.
# 9. If the guess is correct:
#       - Display a success message.
#       - End the game.
# 10. If the guess is incorrect:
#       - Reduce the number of attempts.
#       - Display remaining attempts.
# 11. If all attempts are used:
#       - Display a game over message.
#       - Reveal the correct word.
import random

# List of words and hints
words = {
    "python": "A popular programming language",
    "tiger": "A large wild cat",
    "apple": "A common fruit",
    "india": "A country in Asia",
    "cricket": "A popular sport in India"
}

# Select a random word
secret_word = random.choice(list(words.keys()))

# Get the hint
hint = words[secret_word]

# Number of attempts
attempts = 3

print("=== WORD GUESSING GAME ===")
print("Hint:", hint)

while attempts > 0:

    guess = input("Guess the word: ").lower()

    if guess == secret_word:
        print("Congratulations! You guessed the word correctly.")
        break

    else:
        attempts -= 1

        if attempts > 0:
            print("Wrong guess!")
            print("Attempts left:", attempts)

        else:
            print("Game Over!")
            print("The correct word was:", secret_word)
import random

words = {
    "python": "A popular programming language",
    "tiger" : "A large wild cat",
    "apple": "A common fruit",
    "india": "A country in South Asia",
    "cricket": "A popular sport in India"
}

secret_word = random.choice(list(words.keys()))
hint = words[secret_word]
attempts = 3
print("Word Guessing Game")
print("Hint:", hint)
while attempts > 0:
    guess = input("Enter your guess: ").lower()
    if guess == secret_word:
        print("Congratulations! You guessed the word.")
        break
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")
        if attempts > 0:
            print("wrong guess.!")
            print("Attempts left:", attempts)
        else:
            print("Game Over!")
            print("The correct word was:", secret_word)