from http import client
import socket

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #gets ip address
ADDR = (SERVER, PORT) #binds the server and port in a tuple
FORMAT = 'utf-8'
DISCONNECT_MSG = "[DISCONNECT]"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) 
    send_length += b'' * (HEADER -len(send_length)) #buffers the bytes
    client.send(send_length)
    client.send(message)

send("Hello World!") #should print out hello world in the server