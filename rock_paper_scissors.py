import random


def game():
    user_choice = input(
        "What's your choice? 'r' for rock, 'p' dor paper, 's' for scissors: ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return "It's a tie"

    elif is_win(user_choice, computer_choice):
        return "You beat the computer"

    else:
        return "You lose"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(game())
