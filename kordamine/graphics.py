from tkinter import * #impordib modduli


def run(): #run funktsiooni defineerimine
    name1 = name_storage.get() #
    print(name1) #väljastab nime
    name.delete(0, END) #kustutab nime


screen = Tk() #defineerib screen
screen.title("My first graphics program") #akna pealkiri
screen.geometry("500x500") #akna suurus

welcome_text = Label(text="Welcome to our first graphics program ", fg="red", bg="yellow") #tekst
welcome_text.pack() #

click_me = Button(text="Click me", fg="red", bg="yellow", command=run) #nupu disain
click_me.place(x=10, y=20) #nupu paigutus

name_storage = StringVar()
name = Entry(textvariable=name_storage)
name.pack()
screen.mainloop()