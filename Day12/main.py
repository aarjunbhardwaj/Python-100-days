from art import logo
import random

def guess_number():
    guess_this = random.randint(1,100)
    print("Jai Ram ji ki: ")
    print(logo)
    print("I am thinking number between 1 to 100,try to guess it")
    difficulty = input("choose a difficulty. Type 'easy' or 'hard' : ")
    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5

    while guesses > 0:
        if guesses > 1:
            print(f"you have {guesses} guesses left for the number that I am thinking of.")
        else:
            print(f"last try to guess the number I 'm thinking of")
        attempt = int(input("try to guess: "))
        if attempt > guess_this:
            print("Too high")
        elif attempt < guess_this:
            print("Too low")
        if guesses == 1:
            print("Game Over.")
        elif attempt == guess_this:
            def game_over():
                print(f"correct! the answer was {guess_this}.thanks for completing that")
                return guesses - guesses
            guesses = game_over()
        guesses -= 1
    
    play_again = input("\nDo you want to play again Type 'y' if yes 'n' for quit")
    if play_again == 'y':
        guess_number()
    else:
        print("Good Bye.")
guess_number()        