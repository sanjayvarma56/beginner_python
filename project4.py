#Ask the user to make a choice
#If choice is not valid 
#Print an error
#Let the computer make a choice
#Print choices (emojis)
#Determine the winner
#Ask the user if they want to continue
#If not
#Terminate

#Rock,Paper,Scissors Game using multiple elif statements means for each condition 
import random
emojis = {"r":"✊", "p":"✋", "s":"✌️"}
choices = ["r","p","s"]

print("Welcome to Rock,Paper,Scissors Game")
while True:
    user_score = 0
    computer_choice = 0
    while user_score < 2 and computer_choice < 2:
        print(f"Your_score: {user_score}")
        print(f"Computer_choice: {computer_choice}")
        user_choice = input("Rock, Paper, Scissors?(r/p/s): ")
        if user_choice not in choices:
            print("Invalid choice. Please choose r, p, or s.")
            #break 
            continue
    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    count_tie = 0
    count_win = 0
    count_lose = 0
    if user_choice == computer_choice:
        print("It's a tie!")
        count_tie += 1
    elif user_choice == "r" and computer_choice  == "s":
        print("You win! Rock beats Scissors.")
        count_win += 1
    elif user_choice == "p" and computer_choice == "r":
        print("You win! Paper beats Rock.")
        count_win += 1
    elif user_choice == "s" and computer_choice == "p":
        print("You win! Scissors beats Paper.")
        count_win += 1
    else:
        print("You Lose; Computer wins!")
        count_lose += 1
    print(f"Stats-\nWins: {count_win}, \nLosses: {count_lose}, \nTies: {count_tie}")
    #Winner 
    print("Final Results")
    if user_score == 2:
        print("Congratulations! You won the match!")
    else:
        print("Computer won the match!")
    #Play again
    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == "n":
        break

#Rock,Paper,Scissors Game using single elif statement means for all conditions
import random
emojis = {"r":"🪨", "p":"📄", "s":"✂️"}
choices = ["r","p","s"]

print("Welcome to Rock,Paper,Scissors Game")
while True:
    user_score = 0
    computer_choice = 0
    while user_score < 2 and computer_choice < 2:
        print(f"Your_score: {user_score}")
        print(f"Computer_choice: {computer_choice}")
        user_choice = input("Rock, Paper, Scissors?(r/p/s): ")
        if user_choice not in choices:
            print("Invalid choice. Please choose r, p, or s.")
            #break 
            continue
        computer_choice = random.choice(choices)
        print(f"You chose {emojis[user_choice]}")
        print(f"Computer chose {emojis[computer_choice]}")
        count_tie = 0
        count_win = 0
        count_lose = 0
        if user_choice == computer_choice:
            print("It's a tie!")
            count_tie += 1
        elif (user_choice == "r" and computer_choice  == "s") or \
            (user_choice == "p" and computer_choice == "r") or \
            (user_choice == "s" and computer_choice == "p"):
            print("You win! ")
            count_win += 1
        else:
            print("You Lose; Computer wins!")
            count_lose += 1

        print(f"Stats - \n Wins: {count_win}, \nLosses: {count_lose}, \nTies: {count_tie}")
#Winner 
    print("Final Results")
    if user_score == 2:
        print("Congratulations! You won the match!")
    else:
        print("Computer won the match!")
    #Play again
    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == "n":
        break

#Two player mode
emojis = {"r": "✊", "p": "✋", "s": "✌️"}
choices = ["r", "p", "s"]

print("Welcome to Two Player Rock, Paper, Scissors Game")

while True:
    player1_score = 0
    player2_score = 0
    while player1_score < 2 and player2_score < 2:
        print(f"Player 1 Score: {player1_score}")
        print(f"Player 2 Score: {player2_score}")
        player1 = input("Player 1 - Rock, Paper, Scissors? (r/p/s): ").lower()

        if player1 not in choices:
            print("Invalid choice by Player 1")
            continue

        player2 = input("Player 2 - Rock, Paper, Scissors? (r/p/s): ").lower()

        if player2 not in choices:
            print("Invalid choice by Player 2")
            continue

        print(f"\nPlayer 1 chose {emojis[player1]}")
        print(f"Player 2 chose {emojis[player2]}")

        if player1 == player2:
            print("It's a tie!")

        elif player1 == "r" and player2 == "s":
            print("Player 1 wins! Rock beats Scissors.")
            player1_score += 1
        elif player1 == "p" and player2 == "r":
            print("Player 1 wins! Paper beats Rock.")
            player1_score += 1
        elif player1 == "s" and player2 == "p":
            print("Player 1 wins! Scissors beats Paper.")
            player1_score += 1
        else:
            print("Player 2 wins!")
            player2_score += 1
        print(f"Stats-\nWins: {count_win}, \nLosses: {count_lose}, \nTies: {count_tie}")
#Winner
    print("\nFinal Results")
    if player1_score == 2:
        print("Congratulations! Player 1 won the match!")
    else:        
        print("Congratulations! Player 2 won the match!")
    #Play again
    should_continue = input("\nDo you want to play again? (y/n): ").lower()

    if should_continue == "n":
        print("Thanks for playing!")
        break

#Combination of both single player with computer mode and two player mode
import random

emojis = {"r": "✊", "p": "✋", "s": "✌️"}
choices = ["r", "p", "s"]

print("Welcome to Rock, Paper, Scissors Game")

while True:

    print("\nSelect Game Mode")
    print("1. Single Player")
    print("2. Two Player")
    mode = input("Enter choice (1/2): ")
    if mode == "1":
        user_score = 0
        computer_score = 0
        while user_score < 2 and computer_score < 2:
            print(" New Round ")
            print(f"Your Score: {user_score}")
            print(f"Computer Score: {computer_score}")
            user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
            if user_choice not in choices:
                print("Invalid choice.")
                continue

            computer_choice = random.choice(choices)
            print(f"You chose {emojis[user_choice]}")
            print(f"Computer chose {emojis[computer_choice]}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif user_choice == "r" and computer_choice == "s":
                print("You win this round!")
                user_score += 1
            elif user_choice == "p" and computer_choice == "r":
                print("You win this round!")
                user_score += 1
            elif user_choice == "s" and computer_choice == "p":
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

        # Final Result
        print(" Final result")
        if user_score == 2:
            print("You won the match!")
        else:
            print("Computer won the match!")

    elif mode == "2":

        player1_score = 0
        player2_score = 0

        while player1_score < 2 and player2_score < 2:

            print("\n--- New Round ---")
            print(f"Player 1 Score: {player1_score}")
            print(f"Player 2 Score: {player2_score}")

            player1 = input("Player 1 (r/p/s): ").lower()

            if player1 not in choices:
                print("Invalid choice by Player 1")
                continue

            player2 = input("Player 2 (r/p/s): ").lower()

            if player2 not in choices:
                print("Invalid choice by Player 2")
                continue

            print(f"\nPlayer 1 chose {emojis[player1]}")
            print(f"Player 2 chose {emojis[player2]}")
            if player1 == player2:
                print("It's a tie!")
            elif player1 == "r" and player2 == "s":
                print("Player 1 wins this round!")
                player1_score += 1
            elif player1 == "p" and player2 == "r":
                print("Player 1 wins this round!")
                player1_score += 1
            elif player1 == "s" and player2 == "p":
                print("Player 1 wins this round!")
                player1_score += 1
            else:
                print("Player 2 wins this round!")
                player2_score += 1
#Winner
        print(" Final Result")

        if player1_score == 2:
            print("Player 1 wins the match!")

        else:
            print("Player 2 wins the match!")

    else:
        print("Invalid mode selected.")
        continue
#Play again
    should_continue = input("\nDo you want to play again? (y/n): ").lower()

    if should_continue == "n":
        print("Thanks for playing!")
        break