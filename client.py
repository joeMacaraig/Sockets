from http import client
import socket

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #gets ip address
ADDR = (SERVER, PORT) #binds the server and port in a tuple
FORMAT = 'utf-8'
DISCONNECT_MSG = "_[DISCONNECT]_"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT) 
    send_len += b'' * (HEADER -len(send_len)) #buffers the bytes
    client.send(send_len)
    client.send(message)

send("Hello World!") #should print out hello world in the server