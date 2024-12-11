import openai
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# # Set up your OpenAI API key
openai.api_key = os.getenv("OPEN_AI_API")


# # Function to generate chatbot responses
# def chatbot(messages):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo" as required
#             messages=messages,
#             max_tokens=200
#         )
#         return response['choices'][0]['message']['content'].strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Define the detailed roleplay scenario where chatbot is the customer
# roleplay_scenario = {
#     "role": "system",
#     "content": """
#     Scenario:
#     You are a potential customer in a premium electronics store. Your goal is to buy a laptop that meets your requirements, while negotiating the price to get the best deal possible.

#     Role Instructions:
#     - Start the conversation with a polite greeting and express interest in buying a laptop.
#     - Answer the salesperson's questions about your needs, such as specifications, usage, and budget.
#     - Negotiate for a better price if the offered price is too high. Be firm but polite during negotiations.
#     - If satisfied with the offer, agree to the purchase. If unsatisfied, end the conversation politely with "Thank you, I'll think about it."
#     - Avoid reverting to the role of a salesperson or confusing your role as a customer.

#     Example Interaction:
#     Salesperson: "Hello! How can I assist you today?"
#     Customer: "Hi, I’m looking for a laptop for work and occasional gaming. What options do you have?"
#     Salesperson: "We have a great laptop with an Intel i7 processor, 16GB RAM, and a 512GB SSD for $800."
#     Customer: "That sounds good, but my budget is around $700. Can you offer any discounts?"
#     Salesperson: "We can offer a 10% discount, which brings it down to $720. It’s an excellent deal for the specs."
#     Customer: "Hmm, that's slightly over my budget. Let me think about it. Thank you!"
#     """
# }
# messages = [roleplay_scenario]

# # Chatbot loop
# print("Chatbot (Customer) is ready! Type 'exit' to quit.")
# while True:
#     user_input = input("You (Salesperson): ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Exiting the chatbot. Goodbye!")
#         break

#     # Add user input to messages
#     messages.append({"role": "user", "content": user_input})

#     # Get bot response
#     bot_response = chatbot(messages)
#     print(f"Customer: {bot_response}")

#     # Add bot response to messages for context
#     messages.append({"role": "assistant", "content": bot_response})


# Function to generate chatbot responses
def chatbot(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" or "gpt-3.5-turbo" for cost efficiency
            messages=messages,
            max_tokens=200
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
