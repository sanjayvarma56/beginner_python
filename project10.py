#
# BILL SPLITTER WITH FILE STORAGE
# PROGRAM RULES / FLOW
# 
# 1. Run the program continuously until the user chooses to stop.
# 2. Create an empty list to store member names.
# 3. Ask the user for the number of members.
# 4. Collect the names of all members and store them in the list.
# 5. Ask for:
#       - Total bill amount
#       - Expense name
#       - Name of the person who paid
# 6. Calculate each person's share by dividing
#    the total bill amount by the number of members.
# 7. Display expense details:
#       - Expense name
#       - Total amount
#       - Paid by
# 8. Display how much each person should pay.
# 9. Identify members who did not pay and show
#    how much they owe to the person who paid.
# 10. Return all bill information from split_bill()
#     so it can be used elsewhere in the program.
# 11. Open "bill_splitter.txt" in append mode ("a").
# 12. Add a separator line before saving a new bill.
# 13. Save:
#       - Expense name
#       - Total amount
#       - Paid by
#       - Members list
#       - Split amount
# 14. Save payment details showing who should pay whom.
# 15. Close the file after writing all information.
# 16. Display a success message after saving.
# 17. Ask the user whether they want to split another bill.
# 18. If user enters "no":
#       - Display thank you message.
#       - Exit the program.

# 19. If user enters "yes":
#       - Start a new bill entry.
while True:
    def split_bill():
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
        return members, expense_name, total_bill, paid_by, split_amount
    members, expense_name, total_bill, paid_by, split_amount = split_bill()
    #Save to file
    def save_to_file(members, expense_name, total_bill, paid_by, split_amount):
        e=open("bill_splitter.txt", "a")
        e.write("\n------------------------\n")
        e.write("Expense Details: \n")
        e.write("Expense: " + expense_name + "\n")
        e.write("Total amount: " + str(total_bill) + "\n")
        e.write("Paid By:" + paid_by + "\n")
        e.write("Members: " + ", ".join(members) + "\n")
        e.write("Each Person Pays: " + str(split_amount) + "\n")
        e.write("\nPayment Details:\n")
        for person in members:
                if person != paid_by:
                    e.write(
                    person + " should pay " +
                    str(split_amount) +
                    " to " +
                    paid_by +
                    "\n"
                    )
        print("Bill details saved successfully!")
        e.close()
    save_to_file(members, expense_name, total_bill, paid_by, split_amount)
    add =input("Do you want to split another bill? (yes/no)").lower()
    if add == "no":
        print("Thank you for using the bill splitter!")
        break
