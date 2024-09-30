import fbchat
a=input('enter email : ')
b=input('enter pass : ')
# Replace 'your_email' and 'your_password' with your actual credentials
client = fbchat.Client(a, b)

# Replace 'recipient_user_id' with the user ID of the person you want to message
recipient_id = int(input('enter tid'))

# Send a message
message = fbchat.Message(text='Hello from Python!')
sent_message = client.send(message, thread_id=recipient_id)

print(sent_message)
