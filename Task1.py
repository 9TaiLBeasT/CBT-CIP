#MASTERMIND GAME

def player2_guess():
    return int(input("\nPlayer-2 Guess the number: "))

def player2_set():
    return int(input("Player-2 Set Your Multi Digit Number: "))

def player1_set():
    return int(input("Player-1 Enter Your Multi Digit Number: "))

def player1_guess():
    return int(input("\nPlayer-1 Guess the number: "))

def Hint2(player1set, player2guess):
    player1set = str(player1set)
    player2guess = str(player2guess)
    matching_digits = ""
    
    for digit in player2guess:
        if digit in player1set:
            matching_digits += digit + " "
    
    return matching_digits.strip() if matching_digits else "None"

def Hint1(player2set, player1guess):
    player1guess = str(player1guess)
    player2set = str(player2set)
    matching_digits = ""
    
    for digit in player1guess:
        if digit in player2set:
            matching_digits += digit + " "
    
    return matching_digits.strip() if matching_digits else "None"

# Main game logic
count1 = 0
count2 = 0
correct = True

print("*****************************************************\n*                                                   *\n*           Welcome To MasterMind Game              *\n*                                                   *\n*****************************************************")

while correct:
    count2 += 1
    if count2 == 1:
        p1set = player1_set()
        p2guess = player2_guess()
        if p2guess == p1set:
            print("Player 2, you're a Master Mind!!")
            correct = False
        else:
            print(f"You lost round {count2}")
            hint = Hint2(p1set, p2guess)
            print("Hint:\nYour Matching Digits are: ",hint)
    else:
        p2guess = player2_guess()
        if p2guess == p1set:
            print(f"You have successfully guessed the number in round {count2}.\n")
            p2set = player2_set()
            for i in range(count2):
                p1guess = player1_guess()
                count1 += 1
                if p1guess == p2set and count1 < count2:
                    print("Player 1, you won the game and you're the Master Mind!!")
                    correct = False
                    break
                elif p1guess != p2set:
                    print(f"You lost round {count1}")
                    hint = Hint1(p2set, p1guess)
                    print("Hint:\nYour Matching Digits are:", hint)
                if count1 >= count2:
                    print("Player 1, your chances are over, Player 2 won the game!!")
                    correct = False
                    break
        else:
            print(f"You lost round {count2}")
            hint = Hint2(p1set, p2guess)
            print("Hint:\nYour Matching Digits are:", hint)
