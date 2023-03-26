import os

# Takes in the 
def connect(code1, code2):
    file1 = code1+code2+".txt"
    file2 = code2+code1+".txt"
    if(not os.path.isfile(file1) and not os.path.isfile(file2)):
        make = open(file1, "a+")
        make.close()
        return("%" + "New message from: ")
    elif(not os.path.isfile(file1) and os.path.isfile(file2)):
        read = open(file2, "r")
        str = "Successfully connected, missed messages: " + read.read()
        return(str)
    else:
        return("Already connected!")


def disconnect(code1, code2):
    file1 = code1+code2+".txt"
    os.remove(file1)
    return("Disconnected!")

