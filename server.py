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
MAX_USERS = 5 # Change this to add more clients on the server (More clients == More server stress)

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

            # Sending MSG to other clients
            BroadcastMSG(f'{decodedReceivedNickname} joined!')

            # Main loop
            while True:
                # Receiving MSG from client
                receivedMSG = client.recv(10000)
                decodedReceivedMSG = receivedMSG.decode('utf-8')

                # Checking decodedReceivedMSG
                if decodedReceivedMSG == '/exit':
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
                elif decodedReceivedMSG == '//EXIT//': # EXIT_INFO leak protection
                    # Sending WARNING INFO to the client
                    client.send(f'[WARNING]: You can not do that!'.encode('utf-8'))

                    # Printing WARNING MSG
                    print(f'[WARNING]: {decodedReceivedNickname} tried to leak EXIT_INFO!')
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
