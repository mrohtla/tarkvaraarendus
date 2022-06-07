import socket, sys, time # impordib moodulid

s = socket.socket()
host = input(str("Please enter the hostname of the server: "))#serveri nime sisestus
port = 8083 #pordi number
s.connect((host,port))# seob omavahel hosti ja pordi
print("Connected to chat server") #väljastab teksti
while 1:
    in_message = s.recv(1024)
    in_message = in_message.decode()
    print("Server :", in_message)
    print("")
    message = message.encode()
    s.send(message)
    print("message has been sent")#väljastab teksti
    print("")