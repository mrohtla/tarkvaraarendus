from tkinter import * #impordib mooduli
import time #impordib mooduli
import random #impordib mooduli

winner      = False
red_horse_x = 0 #punane hobune
red_horse_y = 20 #punane hobune

blue_horse_x = -28 #sinine hobune
blue_horse_y = 110 #sinine hobune

def start_game(): #defineerib funktsiooni
    global blue_horse_x
    global red_horse_x
    global winner

    while winner == False:
        time.sleep(0.05)
        random_move_blue_horse = random.randint(0,20)
        random_move_red_horse  = random.randint(0,20)
        blue_horse_x += random_move_blue_horse
        red_horse_x  += random_move_red_horse

        move_horses(random_move_red_horse,random_move_blue_horse)
        main_screen.update()
        winner = check_winner()

    if winner == "Tie": #
        Label(main_screen,text=winner,font=('calibri',20),fg="green").place(x=200,y=450)
    else:
        Label(main_screen,text=winner+" Wins !!",font=('calibri',20),fg="green").place(x=200,y=450)


def move_horses(red_horse_random_move,blue_horse_random_move): #defineerib funktsiooni
    canvas.move(red_horse,red_horse_random_move,0)
    canvas.move(blue_horse,blue_horse_random_move,0)

def check_winner(): #defineerib võitmis funktsiooni
    if blue_horse_x >= 550 and red_horse_x >= 550: #kui hobused jõuavad samal ajal 550
        return "Tie" #viik
    if blue_horse_x >= 550: #kui sinine hobune 550
        return "Blue Horse" #sinine hobune
    if red_horse_x >= 550: #kui punane hobune jõuab 550
        return "Red Horse" #punane hobune
    return False 


main_screen = Tk()
main_screen.title('Horse Racing') #akna pealkiri
main_screen.geometry('600x500') #akna suurus
main_screen.config(background='white') #taust


canvas = Canvas(main_screen,width=600,height=200,bg="white")
canvas.pack(pady=20)


red_horse_img = PhotoImage(file="./images/red-horse.png") #laeb hobuse pildi
blue_horse_img = PhotoImage(file="./images/blue-horse.png") #laeb hobuse pildi


red_horse_img = red_horse_img.zoom(15)
red_horse_img = red_horse_img.subsample(50)
blue_horse_img = blue_horse_img.zoom(15)
blue_horse_img = blue_horse_img.subsample(90)


red_horse = canvas.create_image(red_horse_x,red_horse_y,anchor=NW,image=red_horse_img)
blue_horse = canvas.create_image(blue_horse_x,blue_horse_y,anchor=NW,image=blue_horse_img)


l1 = Label(main_screen,text='Select your horse',font=('calibri',20),bg="white") #tekst
l1.place(x=230,y=280) #paigutab teksti
l2 = Label(main_screen,text='Click play when ready!',font=('calibri',20),bg='white') #tekst
l2.place(x=200,y=330) #paigutab teksti

b1 = Button(main_screen,text='Play!',height=2,width=15,bg='white',font=('calibri',10),command=start_game) #nupp
b1.place(x=250,y=390) #paigutab nupu

main_screen.mainloop()