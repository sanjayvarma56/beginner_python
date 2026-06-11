# Get student name from user
# Get student marks from user
# Check marks and assign Grade A if marks are 90 or above
# Check marks and assign Grade B if marks are between 80 and 89
# Check marks and assign Grade C if marks are between 70 and 79
# Check marks and assign Grade D if marks are between 60 and 69
# Check marks and assign Grade E if marks are between 50 and 59
# Assign Failed if marks are below 50
# Display the assigned grade
# Open the file in append mode so new records are added without deleting existing data
# Create the file automatically if it does not already exist
# Write student name, marks, and grade into the file
# Move to a new line after writing each record
# Automatically close the file after writing
# Display a confirmation message indicating that the record has been saved successfully
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "Failed"

print("Grade:", grade)

with open("student_grades.txt","a") as file:
    file.write(f"Name: {name} , Marks: {marks}, Grade: {grade}\n")
print("Student information saved to student_grades.txt")
print("Record saved successfully")