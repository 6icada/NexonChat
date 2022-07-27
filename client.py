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
        # userInput (Input MSG to send to the server)
        userInput = input()

        # Checking userInput
        if userInput[0] == '/':
            if userInput == '/exit':
                # Sending userInput to the server
                Client_Socket.send(userInput.encode('utf-8'))
                exit()
            elif userInput == '/upload':
                try:
                    # Sending userInput to the server
                    Client_Socket.send(userInput.encode('utf-8'))

                    # userInput (Choose file to upload)
                    userInputFile = input()

                    # Opening file
                    fileToOpen = open(f'{userInputFile}', 'r')
                    dataToSend = fileToOpen.read()
                    fileToOpen.close()

                    # Sending dataToSend
                    Client_Socket.send(dataToSend.encode('utf-8'))

                    # Printing INFO
                    print(f'[INFO]: File uploaded!')
                except:
                    # ERROR MSG
                    print(f'[ERROR]: Can\'t upload file...')
            elif userInput == '/download':
                try:
                    # Sending userInput to the server
                    Client_Socket.send(userInput.encode('utf-8'))

                    # Downloading File
                    receivedDataForFile = Client_Socket.recv(10000000)
                    decodedReceivedDataForFile = receivedDataForFile.decode('utf-8')

                    # Storing decodedReceivedDataForFile
                    fileToStore = open('fileToStore.txt', 'w')
                    fileToStore.write(decodedReceivedDataForFile)
                    fileToStore.close()

                    # Printing INFO
                    print(f'[INFO]: File downloaded!')
                except:
                    # ERROR MSG
                    print(f'[ERROR]: Can\'t download file...')
            elif userInput == '/help':
                # INFO MSG
                print('/upload    -- Upload file to server')
                print('/download  -- Download file from server')
                print('/exit      -- Exit the server')
                print('/help      -- This MSG')
            elif userInput == '//EXIT//':
                # WARNING MSG
                print('[WARNING]: You can not do that! You may demage server!')
                print('[WARNING]: Disconnecting from server for server\'s security...')

                # Disconnecting from the server
                Client_Socket.send('/exit'.encode('utf-8'))
                exit()
            else:
                # ERROR MSG
                print(f'[ERROR]: Command does not exist...')
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
