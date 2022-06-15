#https://github.com/mrohtla/tarkvaraarendus

from tkinter import * #impordib mooduli

def save_info(): #defineerib save_info
    firstname_info = firstname.get() #eesnime info
    lastname_info = lastname.get() #perekonnanime info
    age_info = age.get() #vanuse info
    age_info = str(age_info) #vanuse info stringiks tegemine
    print(firstname_info, lastname_info, age_info) # väljastab eesnime, perekonnanime ja vanuse

    file = open("user.txt", "w") #avab faili
    file.write(firstname_info) #kirjutab eesnime
    file.write(lastname_info) #kirjutab perekonnanime
    file.write(age_info) #kirjutab vanuse
    file.close() #sulgeb faili
    print("User ", firstname_info, "has been registered successfully") #väljastab teksti

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)

screen = Tk()
screen.geometry("500x500") #ekraani suurus
screen.title("Python Form") #ekraani pealkiri
heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "3") #pealkiri
heading.pack()

firstname_text = Label(text="Firstname * ", ) #eesnime välja pealkiri
lastname_text = Label(text="Lastname * ", ) #perekonnanime välja pealkiri
age_text = Label(text="Age * ", ) #vanuse välja pealkiri
firstname_text.place(x=15, y=70) #paigutab teksti
lastname_text.place(x=15, y=140) #paigutab teksti
age_text.place(x=15, y=210) #paigutab teksti

firstname = StringVar()
lastname = StringVar()
age = IntVar()

firstname_entry = Entry(textvariable=firstname, width="30") #välja paigutus
lastname_entry = Entry(textvariable=lastname, width="30") #välja paigutus
age_entry = Entry(textvariable=age, width="30") #välja paigutus

firstname_entry.place(x=15, y=100) #väljade paigutus
lastname_entry.place(x=15, y=180) #välja paigutus
age_entry.place(x=15, y=240) #välja paigutus

register = Button(screen, text="Register", width="30", height="2", command=save_info, bg="grey") #registreerimis nupp
register.place(x=15, y=290) #nupu paigutamine

screen.mainloop()

'''
SERVER2 SAADAB CLIENT2 FAILI !!



MAIN LOOB AKNA KASUTAJA SISTESTAB INFO LUUAKSE KASUTAJA SISESTUSE FAIL SALVESTATAKSE LÕPIKS NÄITAB INFOT
main koodis oli vaja kordus lisada
'''