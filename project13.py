#Password Manager
# PASSWORD MANAGER
# PROGRAM RULES / FLOW
# 1. Ask the user to enter the master password.
# 2. Allow the user to:
#       - Add a new password
#       - View existing passwords
#       - Quit the program
# 3. When adding a password:
#       - Ask for the purpose of the password
#         (Email, GitHub, LinkedIn, Banking, etc.)
#       - Ask for the account name/username.
#       - Ask for the password.
#       - Save all details to passwords.txt.
# 4. Store password records in the format:
#       Purpose|Username|Password
# 5. Open passwords.txt in append mode ("a")
#    so new passwords are added without
#    deleting existing data.
# 6. When viewing passwords:
#       - Open passwords.txt in read mode.
#       - Read all lines from the file.
#       - Remove newline characters using strip().
#       - Split each record using "|" separator.
#       - Display purpose, username and password.
# 7. Continue showing the menu until the user
#    chooses to quit.
# 8. If the user enters an invalid option,
#    display an error message and ask again.

pwd = input("What is  the master password? ")
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data=line.strip()
            purpose,user, passw = data.split("|")
            print("Purpose:", purpose,", User:", user, ", Password:", passw)
def add():
    purpose = input("What is the purpose of this password? ")
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(purpose + "|" + name + "|" + pwd + "\n")
while True:
    mode = input("Would you like to add a new password  or view existing ones(view,add), press q to quit ?").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue