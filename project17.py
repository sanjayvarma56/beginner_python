# BASIC CHATBOT WITH CHAT HISTORY
# PROGRAM RULES / FLOW
# 1. Create a chatbot function.
# 2. Display a welcome message to the user.
# 3. Tell the user how to exit the chatbot.
# 4. Open a file named "chat_history.txt" in append mode.
#    - If the file does not exist, create it.
#    - If the file exists, preserve old chats and add new ones.
# 5. Write a session separator to distinguish
#    different chat sessions.
# 6. Start an infinite loop to keep the chatbot running.
# 7. Ask the user for input and convert it to lowercase.
# 8. Save the user's message in the file.
# 9. Check the user's message using if-elif-else.
# 10. If the user enters:
#       "hello"
#       -> Respond with a greeting.
# 11. If the user enters:
#       "how are you?"
#       -> Respond with a status message.
# 12. If the user enters:
#       "what is your name?"
#       -> Tell the chatbot's name.
# 13. If the user enters:
#       "who created you?"
#       -> Tell who created the chatbot.
# 14. If the user enters:
#       "bye"
#       -> Display a goodbye message.
#       -> Save it in the file.
#       -> Exit the loop.
# 15. For any unknown message:
#       -> Display a default response.
# 16. Print the chatbot's response on the screen.
# 17. Save the chatbot's response in the file.
# 18. Automatically close the file when the
#     with block ends.

def chatbot():
    print("ChatBot: Hello! I am your chatbot.")
    print("ChatBot: Type 'bye' to exit.\n")
    with open("chat_history.txt", "a") as file:
        file.write("\n--- New Chat Session ---\n")
        while True:
            user = input("You: ").lower()
            file.write("You: " + user + "\n")
            if user == "hello":
                response = "Hi! How can I help you?"
            elif user == "how are you?":
                response = "I am fine, thank you!"
            elif user == "what is your name?":
                response = "My name is ChatBot."
            elif user == "who created you?":
                response = "I was created by a team of developers using Python."
            elif user == "bye":
                response = "Goodbye! Have a great day!"
                print("ChatBot:", response)
                file.write("ChatBot: " + response + "\n")
                break
            else:
                response = "I'm sorry, I don't understand that."
            print("ChatBot:", response)
            file.write("ChatBot: " + response + "\n")
chatbot()