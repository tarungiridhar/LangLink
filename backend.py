import os
import requests
import uuid
import json


def translate(msg, lang1, lang2):
    # Add your key and endpoint
    key = "ad13e552a674458f9201e1454bd3267b"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "eastus2"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': lang1,
        'to': [lang2]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': msg
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    #test = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    json_load = (json.loads(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))))
    
    for x in json_load:
        return(x['translations'][0]['text'])
    
#print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
# Takes in the user's number as code1 and who they want to connect to as code2
def connect(code1, code2):
    file1 = code1+code2+".txt"
    file2 = code2+code1+".txt"
    file3 = code1 + ".txt"
    

    # Checks to see if neither user is connected
    if(not os.path.isfile(file1) and not os.path.isfile(file2)):
        x = "\n".join(unread(code1, code2))
        read = open(file3, "r")
        make = open(file1, "a+")
        make.close()
        if (len(x) == 0):
            read.close()
            os.remove(file3)
            return("%" + code1 + " connected!")
        else:
            read.close()
            str = "%" + code1 + " connected, missed messages: " + x
            return(str)
    #Checks to see if user2 is connected
    elif(not os.path.isfile(file1) and os.path.isfile(file2)):
        x = "\n".join(unread(code1, code2))
        read = open(file3, "r")
        make = open(file1, "a+")
        make.close()
        if (len(x) == 0):
            read.close()
            os.remove(file3)
            return("Successfully connected!")
        else:
            read.close()
            str = "Successfully connected, missed messages: " + x
            return(str)
    else:
        return("Already connected!")


def unread(code1, code2):
    file3 = code1 + ".txt"
    original = [line.strip() for line in open(file3)]
    toread = [l for l in original if l.startswith(code2)]
    new = [l for l in original if not l.startswith(code2)]
    os.remove(file3)
    with open(file3, 'w') as fp:
        print(*new, sep='\n', file=fp)
    return toread



def disconnect(code1, code2):
    file1 = code1+code2+".txt"
    os.remove(file1)
    file3 = code1 + ".txt"
    inbox = open(file3, "a+")
    inbox.close()
    return("Disconnected!")

def send(code1, code2, msg):
    file1 = code1+code2+".txt"
    file2 = code2+code1+".txt"
    file3 = code2 + ".txt"
    if (os.path.isfile(file1) and os.path.isfile(file2)):
        return msg + "\n"
    elif (os.path.isfile(file1) and not os.path.isfile(file2) and os.path.isfile(file3)):
        inbox = open(file3, 'a')
        inbox.write(code1 + ": " + msg + "\n")
        inbox.close()
        return "%"
