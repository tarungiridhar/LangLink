from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from backend import *
import os
from twilio.rest import Client
from dotenv import load_dotenv


app = Flask(__name__)


def respond(message):
   response = MessagingResponse()
   response.message(message)
   return str(response)

def text(message, num):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID') #os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.getenv('TWILIO_AUTH_TOKEN') #os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=message,
                     from_='+18663484944',
                     to=num
                 )

#866-348-4944
@app.route("/summary", methods=['GET', 'POST'])
def incoming_sms():
    load_dotenv()
    num = request.values.get('From', None)
    user_id = []

    # Read and Split up info.txt file
    content = open('info.txt',"r")
    str = content.read()
    peeps = str.split("\n")
    for x in range(0, len(peeps)):
        peeps[x] = peeps[x].split(",")
    
    # Check if number exists in list 
    # If it is, store it in user_id and call send
    for x in range(0, len(peeps)):
        # If User exists
        if peeps[x][0] == num:
            body = request.values.get('Body', None)
            # If it is a command
            if (body[0] == '%'):
                # If it is connect
                if (body[1] == 'c'):
                    body = body.split(" ")
                    result = connect(num, body[1])
                    # x.append(body[1])
                    # UPDATE INFO.TXT
                    peeps[x].append(body[1])
                    for y in range(0, len(peeps)):
                        peeps[y] = ','.join(peeps[y])
                    with open('info.txt', 'w') as fp:
                        print(*peeps, sep='\n', file=fp)

                    # If new connection, tell other person you connected
                    if (result[0] == '%'):
                        print()
                        text(result[1:], body[1])
                    else: # You are already connected
                        content.close()
                        return respond(result)
                # If it is disconnect
                if (body[1] == 'd'):
                    body = body.split(" ")
                    peeps[x].pop(len(peeps[x])-1)
                    for y in range(0, len(peeps)):
                        peeps[y] = ','.join(peeps[y])
                    with open('info.txt', 'w') as fp:
                        print(*peeps, sep='\n', file=fp)
                    # UPDATE INFO.TXT
                    content.close()
                    return respond(disconnect(num, body[1]))
            # If it is a regular message
            else:
                msg = send(peeps[x][0], peeps[x][len(peeps[x])-1], body)
                if (len(msg) > 0):
                    text(msg, peeps[x][len(peeps[x])-1])
            content.close()
            return ""
    
    # If it does not exist, create listing
    content = open("info.txt","a")
    body = request.values.get('Body', None)
    newUser = body.split(", ")
    content.write("\n"+num+","+newUser[0]+","+newUser[1])
    content.close()
    content = open(num+".txt", "w")
    content.close()
    return respond("Thank you for Registering!")
    

if __name__ == "__main__":
   app.run(host='localhost', debug=True, port=8080)
