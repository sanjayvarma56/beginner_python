#Bill Splitter
# Create an empty list to store member names
# Ask the user how many members are involved
# Loop to take member names as input
# Take member name from user
# Add the name to the members list
# Ask user for expense name
# Ask user for total expense amount
# float() is used because amount may contain decimal values
# Ask who paid the bill
# Calculate equal share for each member
# Divide total amount by total number of members
# Display expense details heading
# Print expense name
# Print total amount
# Print name of the person who paid
# Display how much each person should pay
# Display balances heading
# Loop through all members
# Check if the current member is not the payer
# The payer does not need to pay themselves
# Display who owes money to the payer
members = []
count = int(input("Enter the number of members: "))
for i in range(count):
    name = input("Enter the name of member: ")
    members.append(name)   
total_bill = float(input("Enter the total bill amount: "))
expense_name = input("Enter the name of the expense: ")
paid_by = input("Enter the name of the member who paid: ")
split_amount = total_bill / len(members)

print("Expense Details: ")
print("Expense: ",expense_name)
print("Total amount: ",total_bill)
print("Paid by: ",paid_by)

print("Each person should pay: ",split_amount)
print(paid_by, "already paid the total bill, so others should pay ")
for person in members:
    if person!=paid_by:
        print(person, "should pay", split_amount, "to", paid_by)