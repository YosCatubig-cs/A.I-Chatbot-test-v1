from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Import line ⚠️
import nltk
nltk.download('punkt_tab')
###

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

# Train the chatbot with some example conversations
trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked.",
    "Thank you!",
    "You're welcome!"
])

# Start a conversation loop
print("Charlie: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Charlie: Goodbye! Have a great day!")
        break
    response = chatbot.get_response(user_input)
    print(f"Charlie: {response}")