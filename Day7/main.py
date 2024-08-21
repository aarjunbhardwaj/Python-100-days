
import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo3)
print("\nTo win, guess the word before the person hangs.\n")

display = ["_"] * word_length
wrong_guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please guess a single letter.")
    elif guess in display or guess in wrong_guesses:
        print("You already guessed this letter. Try another one.")
    else:
        if guess not in chosen_word:
            wrong_guesses.append(guess)
            lives -= 1
            print(f"Incorrect! You have {lives} lives left.")
        else:
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display[i] = guess

        print(" ".join(display))
        print(stages[lives])

        if "_" not in display:
            end_of_game = True
            print("Congratulations! You won!")
            print(logo2)
        elif lives == 0:
            end_of_game = True
            print("Sorry, you lost. The word was " + chosen_word)