#Selector
#Random friend selector to decide who to FaceTime!!!
# 1. Import the random module.
# 2. Create a list containing the names of friends.
# 3. Use random.choice() to randomly select one friend from the list.
# 4. Store the selected friend's name in a variable.
# 5. Display a message asking who should be FaceTimed today.
# 6. Print the randomly selected friend's name.
import random
friends = ["Alice", 
           "Bob", 
           "Charlie",
           "David", 
           "Eve",
           "Olek", 
           "Carmela", 
           "Laura", 
           "Anna", 
           "Keith", 
           "Nadya"
           ]
#random.randint(1,5) -- random integer between 1 and 5
#random.choice(array) -- random element from array
selected = random.choice(friends)
print("who should i facetime today?")
print(selected)