# ---------------------------------------------
# QUIZ GAME RULES / PROGRAM FLOW
# ---------------------------------------------

# 1. Display welcome message to the user

# 2. Run the game continuously using while loop

# 3. Ask the user whether they want to play

# 4. Convert user input to lowercase using lower()

# 5. If user input is not "yes":
#       - display exit message
#       - terminate program using quit()

# 6. If user enters "yes":
#       - start quiz game

# 7. Initialize score variable with 0

# 8. Ask multiple computer-related questions

# 9. For every question:
#       - take user input
#       - convert answer to lowercase
#       - compare with correct answer

# 10. If answer is correct:
#       - print "Correct!"
#       - increment score by 1

# 11. Otherwise:
#       - print "Incorrect!"

# 12. After all questions:
#       - display total correct answers
#       - calculate percentage
#       - display percentage score

#Quiz Game
print("Welcome to the quiz game!")
while True:
    playing = input("Do you want to play (yes/no)? ")

    if playing.lower() != "yes":
        print("Invalid input, may be next time!")
        quit()
    print("Great! Let's start the game.")
    score = 0
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    answer = input("What does GPU stand for?")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does RAM stand for?")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does PSU stand for?")
    if answer.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does ROM stand for?")
    if answer.lower() == "read only memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 5) * 100) + "%.")

    #if playing == "no":
        #print("Thanks for playing!")
        #break