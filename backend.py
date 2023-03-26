import os

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
            os.remove(file3)
            str = "%" + code1 + " connected!"
            return(str)
    #Checks to see if user2 is connected
    elif(not os.path.isfile(file1) and os.path.isfile(file2)):
        x = "\n".join(unread(code1, code2))
        read = open(file3, "r")
        if (len(x) == 0):
            read.close()
            os.remove(file3)
            return("Successfully connected!")
        else:
            read.close()
            os.remove(file3)
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
        inbox = open(file3, 'w')
        inbox.write("\n" + msg)
        inbox.close()
        return "%"
