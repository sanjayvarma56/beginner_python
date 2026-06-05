# PASSWORD STRENGTH CHECKER
# PROGRAM RULES / FLOW
# 1. Ask the user to enter a password.
# 2. Check if the password contains:
#       - Uppercase letter
#       - Lowercase letter
#       - Digit
#       - Special character
# 3. Check the password length.
# 4. Count how many conditions are satisfied.
# 5. Display password strength:
#       - Weak
#       - Medium
#       - Strong
# 6. Give suggestions for improvement.

password = input("Enter a password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()-_=+[]{};:,.<>?/"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char :
        has_special = True
score = 0
if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1          
if has_special:
    score += 1

print("\nPassword Analysis")
print("Length >= 8:", len(password) >= 8)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digit:", has_digit)
print("Special Character:", has_special)

if score <= 2:
    print("\nPassword Strength: Weak")

elif score <= 4:
    print("\nPassword Strength: Medium")

else:
    print("\nPassword Strength: Strong")