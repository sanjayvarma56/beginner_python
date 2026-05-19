#Loop
#Ask: Roll the dice?
#If user enters y 
#Generate two random numbers between 1 and 6
#Print the numbers 
#If user enters n 
#Print Thank you message 
#Terminate 
#Else 
#Print Invalid Choice 


#Using If,elif,else Statements
import random
dice = int(input("How many dice you want to roll?"))
count = 0
choice = input("Roll the dice? (yes/no): ")
if choice.lower() == 'yes':
    if dice <=0 or dice > 2:
        print("Invalid Number of dice")
    elif dice == 1:
        dice1 = random.randint(1,6)
        print("You rolled dice1: ",dice1)
        count += 1
    elif dice == 2:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("You rolled ", dice1, "and ",dice2)
        count += 1
elif choice.lower() == 'no':
    print("Thanks for playing")
else:
    print("Invalid choice")

# Using While loop
import random
playing = True 
while playing:
    choice = input("Roll the dice? (yes/no): ")
    if choice.lower() == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("You rolled ", dice1, "and ",dice2)
        count += 1
    elif choice.lower() == 'no':
        print("Thanks for playing")
        playing = False
    else:
        print("Invalid choice")

#Using break statement
import random 
while True:
    count = 0
    choice = input("Roll the dice? (yes/no): ")
    if choice.lower() == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("You rolled ", dice1, "and ",dice2)
        count += 1
    elif choice.lower() == 'no':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")