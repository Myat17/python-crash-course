# Make program run as long as user wants to continue
# To exit the program, the user can enter 'quit'
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
        print(message)