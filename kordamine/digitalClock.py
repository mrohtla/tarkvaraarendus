from tkinter import Tk #impordib mooduli
from tkinter import Label #impordib mooduli
import time #impordib mooduli
import sys #impordib mooduli

master = Tk() #defineerib master
master.title("Digital Clock") #pealkiri

def get_time(): #defineerib funktsiooni
    timeVar = time.strftime("%I:%M:%S %p") #
    clock.config(text=timeVar)
    clock.after(200,get_time)


Label(master,font=("Arial",30),text="Digital Clock",fg="white",bg="black").pack() #pealkiri
clock = Label(master, font=("Arial",100),bg="black",fg="white") #
clock.pack()

get_time() #käivitab funktsiooni

master.mainloop()