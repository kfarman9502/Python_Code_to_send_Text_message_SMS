from twilio.rest import Client

# Replace these with your Twilio Account SID and Auth Token
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Replace these with your Twilio phone number and the recipient's phone numb
from_number = '+1234567890'
to_number = '+0987654321'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the text message
message = client.messages.create(
    from_=from_number,
    body="Hello from Python using Twilio!",
    to=to_number
)

print("text message sent. SID:", message.sid)
