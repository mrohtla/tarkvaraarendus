import socket #impordib mooduli

s = socket.socket()
host = socket.gethostname() #hostname
port = 8080 #pordi number
s.bind((host,port)) #seob pordi ja hosti
s.listen(1) #kuulab ühte
print(host) #väljastab hostnime
print("waiting for incoming connections ..") #väljastab teksti
conn,addr = s.accept()
print(addr, "Has connected to the server") #väljastab teksti

filename = input(str("Please enter the filename to the file: ")) #faili nime sisestamine
file = open(filename, 'rb') #avab faili
file_data = file.read(1024) # loeb faili
conn.send(file_data) #saadab faili
print("Data has been transmitted successfully") #väljastab teksti
