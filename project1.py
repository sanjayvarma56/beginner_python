""" Python Project -1 -- CAFE MANAGEMENT
Step 1: Geeting the user
Step 2:Showing Menu {"Pizza": 50,"Salad": 30,"Burger":100,"Pop Corn": 150}
STEP 3:Note the item
STEP 4:Check the item in our menu
 if Yes: Add the cost 
 Ask user for anything else
 if Yes: Note the second item
 Check the item in our menu 
 Calculate total cost and display
 if No:End order and Display cost
 if No: Display error message """

menu = {'Pizza': 50,'Salad': 30,'Burger':100,'Pop Corn': 150,'Chicken Puff':100} 
print("Welcome to our Cafe")
print(' Pizza: 50\n Salad: 30\n Burger:100\n Pop Corn: 150\n Chicken Puff:100')
order_item=input('Enter your item: ')
order_total = 0
if order_item in menu:
    order_total+=menu[order_item]
    order = input("Do you want anything else(Yes/No):")
    if order == 'Yes':
        order_item2=input("Enter your second item:")
        if order_item in menu:
            order_total += menu[order_item2]
            print(f'Your order value: {order_total}/-')
    else:
        print(f"Your order_value: {order_total}/-")        
else:
    print('You entered a wrong item')