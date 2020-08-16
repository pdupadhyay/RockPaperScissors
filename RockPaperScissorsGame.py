import random
from tkinter import *


def rps():
    global USER_SCORE
    USER_SCORE = 0
    global COMPUTER_SCORE
    COMPUTER_SCORE = 0
    global USER
    USER = ""
    global COMPUTER
    COMPUTER = ""
    global root
    root = Tk()
    background_image = PhotoImage(file="rps_bg.png")
    background = Label(root, image=background_image, bd=0)
    background.pack()
    root.title("Rock Paper Scissors Game")
    root.geometry("600x600")
    root.configure(bg="Black")


    def computer_choice():
        return random.choice(["Rock", "Paper", "Scissors"])


    def game(u, c):
        global USER_SCORE
        global COMPUTER_SCORE
        player = u
        comp = c
        if player == comp:
            print("Tie Game")
        elif player == "Rock":
            if comp == "Paper":
                COMPUTER_SCORE += 1
            else:
                USER_SCORE += 1
        elif player == "Paper":
            if comp == "Rock":
                USER_SCORE += 1
            else:
                COMPUTER_SCORE += 1
        elif player == "Scissors":
            if comp == "Rock":
                COMPUTER_SCORE += 1
            else:
                USER_SCORE += 1



        txt = Text(master=root, height=4, width=30, bg = "Pink", fg = "Black")
        txt.place(x=180, y=400)
        res = "Your Choice:{p}\nComputer's Choice:{c}\nYour Score:{us}\nComputer's Score:{cs}".format(p=player, c=comp,us=USER_SCORE,cs=COMPUTER_SCORE)
        txt.insert(END, res)
        btn4 = Button(root, height = 1, width = 8, text="Reset", bg = "Brown", command = reset)
        btn4.place(x=150, y=520)
        btn5 = Button(root, height = 1, width = 8, text="Exit", bg = "Brown", command=root.destroy)
        btn5.place(x=370, y=520)


    def rock():
        global USER
        global COMPUTER
        USER = "Rock"
        COMPUTER = computer_choice()
        game(USER, COMPUTER)


    def paper():
        global USER
        global COMPUTER
        USER = "Paper"
        COMPUTER = computer_choice()
        game(USER, COMPUTER)


    def scissors():
        global USER
        global COMPUTER
        USER = "Scissors"
        COMPUTER = computer_choice()
        game(USER, COMPUTER)


    lbl1 = Label(root, text="Choose Rock or Paper or Scissors:", bg = "Orange")
    lbl1.place(x = 200, y = 50)
    btn1 = Button(root, height = 1, width = 8, text="Rock", bg = "Cyan", command=rock)
    btn1.place(x = 250, y = 330)
    btn2 = Button(root, height = 1, width = 8, text="Paper", bg = "Cyan", command=paper)
    btn2.place(x = 400, y = 120)
    btn3 = Button(root, height = 1, width = 8, text="Scissors", bg = "Cyan", command=scissors)
    btn3.place(x = 100, y = 70)

    root.mainloop()



def reset():
    root.destroy()
    rps()


rps()
