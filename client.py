# Code by 6icada
# Project NexonChat

# Tring to import libraries
try:
    import socket
    import threading
except:
    # ERROR MSG
    print(f'[ERROR]: Can\'t import libraries...')
    exit()

# Adding SysINFO Texts
nickIsAlreadyUsed = '[ERROR]: Nickname is already used...'
youJoinedTheServer = '[INFO]: You joined the server!'
exitINFO = '//EXIT//'

# Adding vars
HOST = input('Enter IPv4: ')
PORT = 4444
Nickname = input('Enter nickname: ')
Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tring to connect to the server
try:
    Client_Socket.connect((HOST, PORT))
except:
    # ERROR MSG
    print(f'[ERROR]: Can\'t find the server...')
    exit()

# Sending nickname to the server
Client_Socket.send(Nickname.encode('utf-8'))

# Receiving Answer
receivedAnswer = Client_Socket.recv(2048)
decodedReceivedAnswer = receivedAnswer.decode('utf-8')

# Checking decodedReceivedAnswer
if decodedReceivedAnswer == nickIsAlreadyUsed:
    # Printing decodedReceivedAnswer
    print(decodedReceivedAnswer)
    exit()
elif decodedReceivedAnswer == youJoinedTheServer:
    # Printing decodedReceivedAnswer
    print(decodedReceivedAnswer)
else:
    # ERROR MSG
    print('[ERROR]: Did not understand SysINFO...')
    exit()

# Write function (To write and send MSGs)
def Write():
    while True:
        # userInput
        userInput = input()

        # Checking userInput
        if userInput == '/exit':
            # sending userInput to the server
            Client_Socket.send(userInput.encode('utf-8'))
            exit()
        else:
            # Sending userInput to the server
            Client_Socket.send(userInput.encode('utf-8'))

# Receive function (To receive MSGs)
def Receive():
    while True:
        # Receiving MSG
        receivedMSG = Client_Socket.recv(10000)
        decodedReceivedMSG = receivedMSG.decode('utf-8')

        # Checking decodedReceivedMSG
        if decodedReceivedMSG == exitINFO:
            exit()
        else:
            print(decodedReceivedMSG)

# Making threads
writeThread = threading.Thread(target=Write)
receciveThread = threading.Thread(target=Receive)

# Staring Theads
writeThread.start()
receciveThread.start()