import socket
s=socket.socket()
host=input(str("please enter host address of the sender"))
port=8080
s.connect((host,port))
print("connected...")
