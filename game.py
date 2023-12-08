import random

def get_user_choice():
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_hp = 1000
    computer_hp = 1000

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "You win!":
            computer_hp -= 100
        elif result == "Computer wins!":
            user_hp -= 100

        print(f"User's HP: {user_hp}")
        print(f"Computer's HP: {computer_hp}")

        if user_hp <= 0 or computer_hp <= 0:
            break

if __name__ == "__main__":
    play_game()
