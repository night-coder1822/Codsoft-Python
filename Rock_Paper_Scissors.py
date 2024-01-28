import random

def get_user_choice():
    user_choice = int(input("Choose rock (1), paper (2), or scissors (3): "))
    while user_choice not in [1,2,3]:
        print("Invalid choice. Please choose '1' for rock, '2' for paper, or '3' for scissors.")
        user_choice = int(input("Choose rock (1), paper (2), or scissors (3): "))
    return user_choice

def get_computer_choice():
    return random.choice([1, 2, 3])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 3 and computer_choice == 2) or
        (user_choice == 2 and computer_choice == 1)
    ):
        return "You win!"
        print()
    else:
        return "Computer wins!"
        print()

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You choice : {user_choice}")
    print(f"Computer choice : {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your score: {user_score}, Computer's score: {computer_score}")

    play_again = input("Do you want to play another round? (y/n) : ").lower()
    if play_again != "y":
        break