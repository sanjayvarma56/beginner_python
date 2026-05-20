#Number guessing Game
#Generate a random number between start_range and end_range in which both the ranges will be provided by the user.
#Loop
#Ask user to guess the number
#If not valid number 
#Print an error 
#If number < guess 
#Print too low
#If number > guess 
#print too high 
#Else 
#print well done (Congratulations) 


#1st method using exception handling
import random
best_score = None
start_range = int(input("Enter the start of the range of numbers(Please enter only positive integers): "))
end_range = int(input("Enter the end of the range of numbers(Please enter only positive integers: "))
number = random.randint(start_range, end_range)
max_no_of_guesses = 10
print(f"You have {max_no_of_guesses} attempts to guess the number.")
count = 0
while True:
    if count >= max_no_of_guesses: 
            print("Sorry you are out of attempts. \nThe number was ", number)
            break
    try:
        #guess = input("Guess the number between 1 and 100: ")
        guess = int(input(f"Guess the number between {start_range} and {end_range}: "))
        if guess < number:
            print("Too Low. Try again.")
            count += 1
        elif guess > number:
            print("Too High. try again.")
            count += 1
        else:
            print("Congratulations! You have gueessed the number.")
            print("Attempts used:", count)

        # BEST SCORE UPDATE
        if best_score is None or count < best_score:
            best_score = count
            print("New Best Score!")
            print("Best Score:", best_score)
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break



#2nd method using if,elif,else statements
import random
start_range = int(input("Enter the start of the range of numbers(Please enter only positive integers: "))
end_range = int(input("Enter the end of the range of numbers(Please enter only positive integers: "))
number = random.randint(start_range, end_range)
while True:
    #guess = input("Guess the number between 1 and 100: ")
    guess = input(f"Guess the number between {start_range} and {end_range}: ")
    if not guess.isdigit():
        print("Invalid input. Please enter a valid integer.")
        continue
    guess = int(guess)
    if guess < number:
        print("Too Low. Try again.")
    elif guess > number:
        print("Too High. try again.")
    else:
        print("Congratulations! You have gueessed the number.")
        break


    