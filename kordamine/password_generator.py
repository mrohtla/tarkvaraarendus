import random #impordib mooduli

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()' #kasutatavad sümbolid

while 1: #loop
    password_len=int(input('Enter the length of the password: ')) #parooli pikkuse sisestus
    password_count=int(input('Enter the number of passwords to be generated: ')) #paroolide koguse sisestus
    for x in range (0, password_count): #loob parooli
        password = '' #defineerib parooli
        for x in range (0, password_len): #loob parooli
            password_char = random.choice(chars)
            password = password + password_char
        print('Here is your password: ' ,password) #väljastab parooli