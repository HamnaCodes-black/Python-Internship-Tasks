# Basic Rule-Based Chatbot

# Function to respond to the user
def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "i am fine" or user_input == "i am also fine":
        return "Great! Nice to hear"

    elif user_input == "who are you":
        return "I am PyBot, a simple rule-based chatbot made in Python."

    elif user_input == "what is your name":
        return "My name is PyBot."

    elif user_input == "what can you do":
        return "I can have a simple conversation with you."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    
    elif user_input == "help":
        return "I can chat with you, tell jokes, and tell time."

    else:
        return "Sorry, I don't understand that."


# Welcome message
print("===================================")
print("        BASIC CHATBOT")
print("===================================")
print("Hello! I am PyBot.")
print("You can say: hello, how are you, bye")
print("Type 'bye' to end the conversation.\n")


# Chat loop
while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("PyBot:", response)

    if user_input.lower() == "bye":
        break
