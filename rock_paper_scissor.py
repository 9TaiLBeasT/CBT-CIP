import random

def print_choice(choice):
    if choice == 'rock':
        print(""" Rock!!
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif choice == 'paper':
        print(""" Paper!!
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif choice == 'scissors':
        print(""" Scissors!!
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("You chose:")
    print_choice(user_choice)
    print("Computer chose:")
    print_choice(computer_choice)

    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return winner


print("Welcome to Rock-Paper-Scissors!")
rounds = int(input("How many rounds would you like to play? "))
user_score = 0
computer_score = 0
for _ in range(rounds):
    winner = play_round()
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    
    print(f"Score - You: {user_score}, Computer: {computer_score}")
    print()
if user_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif computer_score > user_score:
    print("Computer wins overall. Better luck next time!")
else:
    print("The game is a tie overall!")