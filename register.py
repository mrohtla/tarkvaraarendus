from tkinter import *  #impordib mooduli


def register_user(): #register_user defineerimine

    username_info = username.get() #võtab väärtuse username väljalt
    password_info = password.get() #võtab väärtuse password väljalt

    file = open(username_info + ".txt", "w") #avab kirjutamiseks faili
    file.write(username_info + "\n") #kirjutab kasutajanime faili
    file.write(password_info) #kirjutab parooli faili
    file.close() #paneb faili kinni

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Sucess", fg = "green", font = ("calibri", 11)).pack() #


def register(): # register funktsiooni defineerimine
    global screen1
    screen1 = Toplevel(screen) # loob ekraani
    screen1.title("Register") #ekraani pealkiri
    screen1.geometry("300x250") #ekraani suurus

#defineerib muutujad
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack() # tekst
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command=register_user).pack()


def login(): #login funktsiooni defineerimine
    print("Login session started") #väljastab teksti


def main_screen(): #main_screen funktiooni defineerimine
    global screen
    screen = Tk() #loob ekraani
    screen.geometry("300x250") # ekraani suurus
    screen.title("Notes 1.0") # ekraani pealkiri
    Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop() #käivitab funktsiooni


main_screen() #käivitab funktsiooni
