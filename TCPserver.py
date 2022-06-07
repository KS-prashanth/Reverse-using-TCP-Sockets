import threading
import socket
host = "127.0.0.1"
port = 4455
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} disco'.encode('utf-8'))
            aliases.remove(alias)
            break


# Find the reversed string
def my_function(x):
  return x[::-1]



# Main function to receive the clients connection




def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        alias2 = my_function(alias)
        print(f'the send message is :  {alias}'.encode('utf-8'))
        print(f'The reversed Meassage is : client  {alias2}'.encode('utf-8'))
        client.send(f'The reversed Meassage : server {alias2}'.encode('utf-8'))
       
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()