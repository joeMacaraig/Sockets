#Sockets in Python 
import socket 
import threading

from PythonSockets.client import DISCONNECT_MSG, SERVER 

"""

"""

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "_[DISCONNECTED]_"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): 
    print(f"_[NEW CONENCTION]_ {addr} connected...")
    connected = True 
    while connected: 
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len: 
            msg_len = int(msg_len)
            msg = conn.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
        conn.close()

def start():
    server.listen()
    print(f"_[LISTENING]_")
    while True: 
        conn, addr = server.accept() #wait for new connection, store address and object
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print(f"[STARTING] Server {SERVER} is Starting ...")
start()