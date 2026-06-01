# LOGIN AUTHENTICATION SYSTEM
# PROGRAM RULES / FLOW
# 1. Import the time module.
# 2. Store the correct username and password.
# 3. Ask the user to enter a username.
# 4. Ask the user to enter a password.
# 5. Check if both username and password are correct.
# 6. If both are correct:
#       - Display login successful message.
#       - Pause program for 5 seconds.
#       - Display loading messages.
#       - Use time.sleep() to simulate loading.
#       - Grant security clearance.
# 7. If username is correct but password is incorrect:
#       - Display incorrect password message.
# 8. If password is correct but username is incorrect:
#       - Display incorrect username message.
# 9. If both username and password are incorrect:
#       - Display error message.

import time
username = "saisanju"
password = "saisanju123"
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
if username_input == username and password_input == password:
    print("Login successful!")
    print("Please wait")
    time.sleep(5)
    print("Ok... Loading...")
    time.sleep(2)
    print("....")
    time.sleep(1)
    print("....")
    print("Alright you hve security clearance. Pulling up the secret mainframe")
elif username_input == username and password_input != password:
    print("Incorrect password. ")
elif username_input != username and password_input == password:
    print("Incorret Username")
else:
    print("You might wanna check the fields....")
