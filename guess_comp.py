import random


def guess():
    random_number = random.randint(1, 50)
    guess_number = 0
    while (random_number != guess_number):
        guess_number = int(input("Enter your guess between 1 and 50:"))
        if random_number > guess_number:
            print("Too low. Guess Again")
        elif random_number < guess_number:
            print("Too high. Guess Agian")
    print(f"Good Job. {guess_number} is the correct guess")


guess()
