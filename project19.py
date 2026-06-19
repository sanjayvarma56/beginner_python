#PyBank - Simple banking app
#Features

# 1. Deposit money (supports decimal amounts)
# 2. Withdraw money (cannot exceed available balance)
# 3. Check current balance
# 4. View transaction history
# 5. Show total deposits and withdrawals
# 6. Menu-based navigation with confirmation messages
# 7. Exit option to close the programs

balance = 0.0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f'Deposited {amount}/-').lower()
    print(f"{amount} deposited successfully")

def withdraw(amount):
    global balance
    if balance < amount:
        print("Insufficient balance")
    else:
        balance -= amount
        transactions.append(f'Withdrawn {amount}/-').lower()
        print(f"{amount} withdrawn successfully")

def checkBalance():
    global balance
    print(f"Current balance is: {balance}\n ")

def transactionHistory():
    if not transactions:
        print("No transactions yet")
    else:
        print("----Transaction History----")
        for t in transactions:
            print("-",t)
        countd = 0
        countw = 0
        for t in transactions:
            if "Deposited" in t.lower():
                countd += 1
                deposits = countd
            if "Withdrawn" in t.lower():
                countw += 1
                withdrawals = countw
            print(f"\n Total deposits: {deposits}")
            print(f"\n Total withdrawals: {withdrawals}")

#OR
#def transactionHistory():
#    if not transactions:
#        print("No transactions yet")
#    else:
#        print("----Transaction History----")
#        for t in transactions:
#            print("-",t)
#deposits = sum(1 for t in transactions if "Deposited" in t)
#withdrawals = sum(1 for t in transactions if "Withdrawn" in t))
#print(f"Total deposits: {deposits}")
#print(f"Total withdrawals: {withdrawals}")

        
def menu():
    while True:
        print("----PyBank Menu----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5.Exit")

        choice = input("Enter your choice:")
        
        if choice == '1':
            amount = float(input("Enter your amount to deposit: "))
            deposit(amount)
        elif choice == '2':
            amount = float(input("Enter your amount to withdraw: "))
            withdraw(amount)
        elif choice == '3':
            checkBalance()
        elif choice == '4':
            transactionHistory()
        elif choice == 5:
            print("Thank you for using PyBank.Bye")
            break
        else:
            print("Invalid choice")

menu()