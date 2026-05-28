#Choose your own adventure game
# 1. Ask the player to enter their name.
# 2. Display welcome message using player's name.
# 3. Ask player to choose a direction:
#       - left
#       - right
# 4. Convert user input to lowercase using lower()
#    to avoid case sensitivity problems.
# 5. If player chooses "left":
#       - player reaches a river.
# 6. Ask player whether to:
#       - swim across river
#       - walk around river
# 7. If player chooses "swim":
#       - player is eaten by alligator
#       - game over
# 8. If player chooses "walk":
#       - player runs out of water
#       - game over
# 9. If player enters invalid option:
#       - display invalid option message
#       - player loses
# 10. If player chooses "right":
#        - player reaches a bridge.
# 11. Ask player whether to:
#        - cross bridge
#        - go back
# 12. If player chooses "back":
#        - player loses game
# 13. If player chooses "cross":
#        - player meets stranger.
# 14. Ask player whether to:
#        - talk to stranger
#        - ignore stranger
# 15. If player chooses "yes":
#        - stranger gives gold
#        - player wins game
# 16. If player chooses "no":
#        - stranger attacks player
#        - player loses game
# 17. If invalid option entered:
#        - player loses game
# 18. If player enters invalid first direction:
#        - display invalid option message
#        - player loses game
# 19. Display thank you message using player's name.
# - input()
# - print()
# - variables
# - if / elif / else
# - nested conditions
# - string methods
# - lower()
# - user interaction
# - decision-based game logic
name = input("Enter your name: ")
print("Welcome" , name, "to this adventure!")
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right.Which way would yu like to go ? ").lower()
if answer == "left":
    answer == input("You come to a river, you can walk around it or swim across?Type walk to walk around and swim to swim across: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")         
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose.")         
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":    
            print("You ignore the stranger and they are offended. They attack you and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
            print("Not a valid option. You lose.")
else:
        print("Not a valid option. You lose.")
print("Thank you for trying", name)