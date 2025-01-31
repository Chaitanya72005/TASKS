# Define a function to get a response from the chatbot
def get_response(input_text):
    # Convert the input to lowercase
    input_text = input_text.lower()
    
    # Check if the input contains a greeting
    if "hello" in input_text or "hi" in input_text:
        return "Hi there!"
    
    # Check if the input contains a question
    if "?" in input_text:
        return "I'm sorry, I can only answer simple questions."
    
    # If the input doesn't match any of the above, return a default response
    return "I'm sorry, I didn't understand what you said."

# Loop until the user types "bye"
while True:
    # Get input from the user
    user_input = input("You: ")
    
    # Exit the loop if the user types "bye"
    if user_input.lower() == "bye":
        break
    
    # Get a response from the chatbot
    bot_response = get_response(user_input)
    
    # Print the response from the chatbot
    print("Bot:", bot_response)
