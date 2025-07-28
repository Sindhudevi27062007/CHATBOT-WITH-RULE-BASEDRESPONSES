def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there! How can I help you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot 1.0, your virtual assistant.")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        
        elif "help" in user_input:
            print("Chatbot: Sure! I'm here to help. You can ask about weather, time, or general questions.")
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}.")

        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but it's always sunny in here ☀️.")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        else:
            print("Chatbot: I'm not sure I understand. Can you please rephrase?")

# Run the chatbot
chatbot()
