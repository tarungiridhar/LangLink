from twilio.rest import Client

account_sid = 'AC76217e0fdeeb9e08424acdfb6b496a3c'
auth_token = '7e4098c656f719d0e6515ece272f7e04'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18663484944',
  body='po',
  to='+13013666563'
)

print(message.sid)