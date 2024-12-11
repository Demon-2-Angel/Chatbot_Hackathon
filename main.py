from chatbot import chatbot
from evaluate import evaluate_user_response
from database import setup_database, save_conversation, close_database

# Define the concise roleplay scenario where chatbot is the customer
roleplay_scenario = {
    "role": "system",
    "content": """
    You are a customer in a premium electronics store. Your goal is to buy a laptop and negotiate for the best deal possible. 
    Answer questions about your preferences, such as specifications, usage, and budget. Negotiate politely but firmly, and if 
    unsatisfied, end with 'Thank you, I'll think about it.'
    """
}
messages = [roleplay_scenario]

# Maximum number of exchanges to keep in the history
max_history = 10

# Initialize database
setup_database()

# Chatbot loop
print("Chatbot (Customer) is ready! Type 'exit' to quit.")
try:
    while True:
        user_input = input("You (Salesperson): ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break

        # Add user input to messages
        messages.append({"role": "user", "content": user_input})

        # Truncate message history to control token usage
        if len(messages) > max_history + 1:  # +1 to include the system prompt
            messages = [messages[0]] + messages[-max_history:]

        # Get bot response
        bot_response = chatbot(messages)
        print(f"Customer: {bot_response}")

        # Add bot response to messages for context
        messages.append({"role": "assistant", "content": bot_response})

        # Evaluate user input
        evaluation = evaluate_user_response(user_input)

        # Save conversation and evaluation to database
        save_conversation(user_input, bot_response, evaluation)

        # Print evaluation (for demonstration purposes)
        print(f"Evaluation: {evaluation}")

finally:
    # Close the database connection
    close_database()
