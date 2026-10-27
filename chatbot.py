
def chatbot():
    print("==============================")
    print("     Welcome to AyushBot!")
    print("==============================")
    print("Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input in ["your name", "what is your name"]:
            print("Bot: My name is AyushBot!")

        elif user_input == "help":
            print("Bot: Try saying hello, asking my name,")
            print("or typing 'how are you'.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

        print()

chatbot()
