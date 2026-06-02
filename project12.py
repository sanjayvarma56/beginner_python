# STUDENT GRADE CALCULATOR
# PROGRAM RULES / FLOW

# 1. Ask the user to enter their marks.
# 2. Check if marks are greater than or equal to 90.
#    If yes, assign Grade A.
# 3. If marks are less than 90, check if they are
#    greater than or equal to 80.
#    If yes, assign Grade B.
# 4. If marks are less than 80, check if they are
#    greater than or equal to 70.
#    If yes, assign Grade C.
# 5. If marks are less than 70, check if they are
#    greater than or equal to 60.
#    If yes, assign Grade D.
# 6. If marks are less than 60, check if they are
#    greater than or equal to 50.
#    If yes, assign Grade E.
# 7. If marks are below 50,
#    display "Failed".

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Failed")