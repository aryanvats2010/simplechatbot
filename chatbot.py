import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk

# Ensure that NLTK data is downloaded
nltk.download('punkt')

# Simple chatbot pairs (patterns and responses)
chat_pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm good, how about you?", "I'm doing well!"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]),
    (r"(.*)", ["I'm sorry, I don't understand that.", "Can you please clarify?"])
]

# Initialize the chatbot
chatbot = Chat(chat_pairs, reflections)

# Function to process the input and get a response
def get_response():
    user_input = user_input_field.get()
    response = chatbot.respond(user_input)
    
    # Temporarily enable the chat log to insert the response
    chat_log.config(state=tk.NORMAL)
    
    # Display user input and bot response in the chat log
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "Bot: " + response + "\n")
    
    # Disable the chat log to prevent user editing
    chat_log.config(state=tk.DISABLED)
    
    # Clear the user input field after sending
    user_input_field.delete(0, tk.END)
    
    # Automatically scroll to the bottom of the chat log
    chat_log.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a scrollable chat log area
chat_log = tk.Text(root, height=20, width=50, state=tk.DISABLED)
chat_log.grid(row=0, column=0, padx=10, pady=10)

# Create the user input field
user_input_field = tk.Entry(root, width=40)
user_input_field.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send the message
send_button = tk.Button(root, text="Send", width=20, command=get_response)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
