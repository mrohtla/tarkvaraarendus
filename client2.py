import socket #impordib moodulid

s = socket.socket()
host = input(str("Please enter the host address of the sender:")) #hostnime sisestamine
port = 8080 #podi number
s.connect((host,port)) #serveri host ja port
print("connected") #väljastab teksti

filename = input(str("Please enter a for the incoming file: ")) #faili nime sisestamine
file = open(filename, 'wb') #avab faili
file_data = s.recv(1024)
file.write(file_data) #kirjutab faili
file.close() #sulgeb faili
print("file has been recieved successfully") #väljastab teksti