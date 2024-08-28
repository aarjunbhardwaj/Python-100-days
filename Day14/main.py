from art import logo, vs
from game_data import data
import random

def profile():
    random_number = random.randint(0, 49)
    name = data[random_number]['name']
    follower_count = data[random_number]['follower_count']
    description = data[random_number]['description']
    country = data[random_number]['country']
    compare = (f"{name}, a {description}, from {country}.")
    return compare, follower_count

def higher_lower():
    score = 0
    correct = True
    while correct:
        profile_a, follower_a = profile()
        profile_b, follower_b = profile()
        while profile_a == profile_b:
            profile_b, follower_b = profile()

        print(logo)
        if score > 0:
            print(f"Your current score is: {score}")
        print(f"Compare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")
        a_or_b = input("\nWho do you think has more followers? Type 'a' or 'b': ").lower()

        if a_or_b == 'a' and follower_a >= follower_b:
            score += 1
            profile_b, follower_b = profile()
        elif a_or_b == 'b' and follower_a <= follower_b:
            score += 1
            profile_a, follower_a = profile()
        elif a_or_b == 'a' and follower_a < follower_b:
            print(f"\nIncorrect, your final score is {score}.")
            correct = False
        elif a_or_b == 'b' and follower_a > follower_b:
            print(f"\nIncorrect, your final score is {score}.")
            correct = False

    play_again = input("\nDo you want to play again? Type 'yes' or 'no': ")
    if play_again == 'yes':
        higher_lower()
    elif play_again == 'no':
        print("Thanks for playing.")

higher_lower()
