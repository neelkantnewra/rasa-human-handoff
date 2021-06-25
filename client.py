import socket
s = socket.socket()
host = 'localhost'
port=1234 
s.connect((host,port))
print("connected to server")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode() 
    print("Server:>>", incoming_message)
    message = input(str("You:>>"))
    message = message.encode()
    s.send(message)
