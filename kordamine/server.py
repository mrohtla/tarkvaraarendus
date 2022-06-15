import socket, sys, time #impordib moodulid

s = socket.socket() #s on socket.socket funktioon
host = socket.gethostname() #hostname'iks arvuti nimi
print("server will start on host: ", host) #väljastab hostnime
port = 8083# pordi number
s.bind((host,port)) #seob hosti ja pordi omavahel
print("") # väljastab tühja rea
print("Server done binding to host and port successfully") #väljasatab teksti
print("")# väljastab tühja rea
s.listen(1)#kuulab ainult ühte porti
conn, addr = s.accept()
print(addr,"Has connected to the server and is now online")#väljastab teksti
print("")# väljastab tühja rea

while 1: #
    message = input(str(">> ")) #sõnumi sisestus
    message = message.encode()
    conn.send(message)#saadab sõnumi
    print("message has been sent") #väljastab teksti
    print("")# väljastab tühja rea
    in_message = conn.recv(1024)#
    in_message = in_message.decode()
    print("Client :", in_message) #kliendi sõnum
    print("")# väljastab tühja rea