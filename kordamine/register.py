#https://github.com/mrohtla/tarkvaraarendus

from tkinter import *  #impordib mooduli
import os #impordib mooduli

def delete2(): #funktsiooni defineerimine
    screen3.destroy() #kustutab väljundi

def delete3(): #funktsiooni defineerimine
    screen4.destroy() #kustutab väljundi

def delete4(): #funktsiooni defineerimine
    screen5.destroy() #kustutab väljundi

def login_success(): #funktsiooni defineerimine
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Succsess") #määrab akna pealkirja
    screen2.geometry("150x100") #määrab akna suuruse
    Label(text="Login success").pack()
    Button(text="OK", command=delete2)

def password_not_recognised(): #funktsiooni defineerimine
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success") #määrab akna pealkirja
    screen4.geometry("150x100") #määrab akna suuruse
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found(): #funktsiooni defineerimine
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success") #akna pealkiri
    screen5.geometry("150x100") #akna suurus
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user(): #funktsiooni defineerimine

    username_info = username.get() #võtab väärtuse username väljalt
    password_info = password.get() #võtab väärtuse password väljalt

    file = open(username_info + ".txt", "w") #avab kirjutamiseks faili
    file.write(username_info + "\n") #kirjutab kasutajanime faili
    file.write(password_info) #kirjutab parooli faili
    file.close() #paneb faili kinni

    username_entry.delete(0, END) #kustutab kasutaja nime
    password_entry.delete(0, END) #kustutab kasutaja parooli

    Label(screen1, text = "Registration Sucess", fg = "green", font = ("calibri", 11)).pack() #

def login_verify(): #funktsiooni defineerimine
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END) #kustutab kasutaja nime
    password_entry1.delete(0, END) #kustutab kasutaja parooli

    list_of_files = os.listdir() #loob nimekirja
    if username1 in list_of_files: #kontrollib kas kasutaja on olemas
        file1 = open(username1, "r") #avab faili
        verify = file1.read().splitlines #loob faili
        if password in verify: #kontrollib kas parool on olemas
            login_success() #kasutab login_success funktsiooni
        else: #kui parooli ei ole
            password_not_recognised() #kasutab password_not_recognised funktsiooni
    else: #kui kasutajat ei ole
        user_not_found() #kasutab user_not_found funktsiooni


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
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login") #akna pealkiri
    screen2.geometry("300x250") #akna suurus
    Label(screen2, text="Please enter details below to login").pack()  # tekst
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username * ").pack()
    username_entry1 =Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=register_user).pack()



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
