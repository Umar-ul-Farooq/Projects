import random
print("Hi welcome to the gueesing game. I will guess the number in your mind.")


def computer_guess():
    print("Give a low and high for me to guess")
    low = int(input("low: "))
    high = int(input("High: "))
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        print(f'Hey, is {guess} the number you had in mind?')
        feedback = (
            input("if correct press 'C', if high press 'H', if lower press 'L': ")).lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay, Good job, the number {guess} is the correct number")


computer_guess()
