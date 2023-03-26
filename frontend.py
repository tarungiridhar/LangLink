from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)


def respond(message):
   response = MessagingResponse()
   response.message(message)
   return str(response)

#866-348-4944
@app.route("/summary", methods=['GET', 'POST'])
def incoming_sms():
    num = request.values.get('From', None)
    user_id = []

    # Read and Split up
    content = open('info.txt',"r")
    str = content.read()
    peeps = str.split("\n")
    for x in range(0, len(peeps)):
        peeps[x] = peeps[x].split(",")
    
    # Check if number exists in list 
    # If it is, store it in user_id
    for x in peeps:
        if x[0] == num:
            user_id = x
            return respond(num)
    
    # If it does not exist, create listing
    content = open("info.txt", "w")


if __name__ == "__main__":
   app.run(host='localhost', debug=True, port=8080)
