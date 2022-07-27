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

# Adding vars
HOST = '0.0.0.0' # Change this if you want specific IPv4 address
PORT = 4444
Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
counter1 = 1
MAX_USERS = 5

# Adding lists
clients = []
threads = []
nicknames = []

# Binding Server_Socket
Server_Socket.bind((HOST, PORT))
Server_Socket.listen()

# MSG when server starts
print(f'[START]: Server listening on {HOST}:{PORT}')

# Handle function (This function will handle one client at the time)
def Handle():
    while True:
        while True:
            # Receiving INFO about client
            client, address = Server_Socket.accept()

            # BroadcastMSG function (This will send MSGs to other clients)
            def BroadcastMSG(msg):
                for Client in clients:
                    if Client == client:
                        pass
                    else:
                        Client.send(msg.encode('utf-8'))

            # Receiving Nickname
            receivedNickname = client.recv(16)
            decodedReceivedNickname = receivedNickname.decode('utf-8')

            # Checking decodedReceivedNickname
            if decodedReceivedNickname in nicknames:
                # Sending ERROR MSG To the client
                client.send(f'[ERROR]: Nickname is already used...'.encode('utf-8'))
                break
            else:
                # Adding decodedReceivedNickname in nicknames list
                nicknames.append(decodedReceivedNickname)

            # Adding clinet in clients list
            clients.append(client)

            # Sending INFO MSG to the client
            client.send(f'[INFO]: You joined the server!'.encode('utf-8'))

            # Printing INFO
            print(f'[INFO]: {decodedReceivedNickname} joined!')

            # Sending WELCOME MSG to the client
            client.send(f'[WELCOME]: Welcome to the Nexon Server!Please do not spam...Have fun <3\n'.encode('utf-8'))

            # Sending USERS to the client
            if len(clients) == 5:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}, {nicknames[2]}, {nicknames[3]}, {nicknames[4]}'.encode('utf-8'))
            elif len(clients) == 4:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}, {nicknames[2]}, {nicknames[3]}'.encode('utf-8'))
            elif len(clients) == 3:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}, {nicknames[2]}'.encode('utf-8'))
            elif len(clients) == 2:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}'.encode('utf-8'))
            elif len(clients) == 1:
                client.send(f'[USERS]: {nicknames[0]}'.encode('utf-8'))

            # Sending MSG to other clients
            BroadcastMSG(f'{decodedReceivedNickname} joined!')

            # Main loop
            while True:
                # Receiving MSG from client
                receivedMSG = client.recv(10000)
                decodedReceivedMSG = receivedMSG.decode('utf-8')

                # Checking decodedReceivedMSG
                if decodedReceivedMSG[0] == '/':
                    if decodedReceivedMSG == '//EXIT//':
                        # Sending WARNING INFO to the client
                        client.send(f'[WARNING]: You can not do that!'.encode('utf-8'))

                        # Printing WARNING MSG
                        print(f'[WARNING]: {decodedReceivedNickname} tried to leak EXIT_INFO!')
                    elif decodedReceivedMSG == '/exit':
                        # Sending EXIT_INFO to the client (This MSG will turn off 'Receive' function on client side)
                        client.send('//EXIT//'.encode('utf-8'))

                        # Removing client's INFO from lists
                        nicknames.remove(decodedReceivedNickname)
                        clients.remove(client)

                        # Printing INFO
                        print(f'[INFO]: {decodedReceivedNickname} left!')

                        # Sending MSG to other clients
                        BroadcastMSG(f'{decodedReceivedNickname} left!')
                        break
                    elif decodedReceivedMSG == '/upload':
                        # Receiving File
                        receivedDataForFile = client.recv(10000000)
                        decodedReceivedDataForFile = receivedDataForFile.decode('utf-8')

                        # Storing decodedReceivedDataForFile in File
                        uploadedFile = open('uploadedFile.txt', 'w')
                        uploadedFile.write(decodedReceivedDataForFile)
                        uploadedFile.close()

                        # Printing INFO
                        print(f'[INFO]: {decodedReceivedNickname} uploaded file!')

                        # Sending INFO to other clients
                        BroadcastMSG(f'[INFO]: {decodedReceivedNickname} uploaded file!')
                    elif decodedReceivedMSG == '/download':
                        # Reading File
                        toDownloadFile = open('uploadedFile.txt', 'r')
                        dataToSend = toDownloadFile.read()

                        # Sending dataToSend to the client
                        client.send(dataToSend.encode('utf-8'))

                        # Printing INFO
                        print(f'[INFO]: {decodedReceivedNickname} downloaded file!')

                        # Sending INFO to other clients
                        BroadcastMSG(f'[INFO]: {decodedReceivedNickname} downloaded file!')
                else:
                    # Sending MSG to other clients
                    BroadcastMSG(f'{decodedReceivedNickname}: {decodedReceivedMSG}')

# Making threads
while counter1 <= MAX_USERS:
    handleThread = threading.Thread(target=Handle)

    threads.append(handleThread)

    counter1 = counter1 + 1

# Starting threads
for thread in threads:
    thread.start()
