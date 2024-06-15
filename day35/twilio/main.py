from twilio.rest import Client

account_sid = ''
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="",
    from_='+18038642107',
    to='+380'
)
# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Your appointment is coming up on July 21 at 3PM',
#   to='whatsapp:+380'
# )
print(message.sid)
# pip install twilio
