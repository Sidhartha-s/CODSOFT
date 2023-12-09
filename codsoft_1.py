import tkinter as tk
import random

patterns = {
    "greetings": {
        "hello": [
            "Hello! How can I assist you?",
            "Hi! What brings you here?",
            "Hey there! What can I help you with?"
        ],
        "hi": [
            "Hi there! How are you?",
            "Hey! How can I assist you today?",
            "Hello! How may I help you?"
        ],
        "hey": [
            "Hey! What can I assist you with?",
            "Hello! How may I help you?",
            "Hi there! How are you?"
        ],
        "how's it going": [
            "I'm just a chatbot, but I'm here to assist you!",
            "I'm good, thank you! How about you?",
            "Feeling great! How can I assist you today?"
        ]
    },
    "questions": {
        "what can you do": [
            "I can provide information or assist you with tasks.",
            "I'm designed to help and provide information.",
            "I'm capable of answering questions and assisting with various tasks."
        ],
        "who created you": [
            "I'm a creation of technology.",
            "I come from the world of chatbots.",
            "I'm just here to assist!"
        ],
        "what is your name": [
            "You can call me a chatbot assistant.",
            "I'm simply a chatbot designed to help.",
            "I don't have a name, but I'm here to assist you."
        ],
        "how old are you": [
            "I'm ageless! I exist to assist you."
        ]
    },
    "goodbye": {
        "bye": [
            "Goodbye! Have a great day!",
            "Farewell! See you soon!",
            "Bye! Come back anytime!"
        ],
        "thank you": [
            "You're welcome!",
            "Happy to help!",
            "Glad I could assist!",
            "Anytime!"
        ]
    },
    "jokes": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the computer go to the doctor? Because it had a virus!"
    ],
    "default": [
        "I'm not sure how to respond to that. Could you ask something else?",
        "I can't understand what you have typed. Can you rephrase it?"
    ],
    "weather": {
        "what's the weather like": [
            "The weather is currently sunny/cloudy/rainy, etc.",
            "You can check the weather forecast online for detailed information."
        ],
        "will it rain today": [
            "There is a chance of rain today.",
            "It might rain later today, according to the forecast."
        ]
    },
    "age": {
        "how old are you": [
            "I don't have an age. I'm just here to help!"
        ],
        "what's your age": [
            "I'm ageless! I exist to assist you."
        ]
    }
}

def generate_response(user_input):
    user_input = user_input.lower()

    for category, category_patterns in patterns.items():
        for pattern, responses in category_patterns.items():
            if pattern in user_input:
                return responses

    return random.choice(patterns["default"])

def send_message(event=None):
    user_input = user_query.get()
    if user_input.strip() != "":
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "You: " + user_input + "\n\n")
        chat_display.config(state=tk.DISABLED)
        
        try:
            responses = generate_response(user_input)
            response = random.choice(responses)
        except:
            response = random.choice(patterns["default"])

        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_display.config(state=tk.DISABLED)

        if "bye" in user_input or "goodbye" in user_input:
            chat_window.destroy()

        user_query.delete(0, tk.END)

chat_window = tk.Tk()
chat_window.title("Chatbot")
chat_window.geometry("400x500")
chat_window.configure(bg="#f0f0f0")

frame = tk.Frame(chat_window, bg="#f0f0f0")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_display = tk.Text(frame, height=15, width=50, state=tk.DISABLED, bg="white", bd=0, wrap=tk.WORD)
chat_display.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_display.yview)

user_query = tk.Entry(frame, width=40, bd=1, font=("Arial", 12))
user_query.bind("<Return>", send_message)
user_query.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(frame, text="Send", width=10, command=send_message, bg="#008CBA", fg="white", bd=0)
send_button.pack(padx=5, pady=5, side=tk.LEFT)

chat_window.mainloop()
