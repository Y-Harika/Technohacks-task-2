import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def main():
    print("Let's play Rock, Paper, Scissors!")
    print("Enter your choice (rock, paper, or scissors) or type 'quit' to exit.")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        print(winner)

if __name__ == "__main__":
    main()