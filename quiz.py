from tkinter import *
#from PIL import ImageTk, Image
import os

class BuddyQuiz:
    
    #CONSTANTS
    FONT_PLAYER = ("Arial", 20, "bold")
    FONT_SCORE = ("Arial", 16)
    FONT_BUTTONS = ("Arial", 16, "bold")
    
    #ROOT SETTINGS
    root = Tk()
    root.title("Buddy Quiz v0.1")
    root.geometry("700x480")
    
    #LABELS, SCORE
    playerString = "PLAYER 1"
    p1score = 0
    p2score = 0
    
    L = Label(root, font=FONT_PLAYER, text=playerString, fg="blue")
    L.pack()
    S1 = Label(root, text="Player 1 Score: " + str(p1score), fg="blue", font=FONT_SCORE)
    S1.pack()
    S2 = Label(root, text="Player 2 Score: " + str(p2score), fg="red", font=FONT_SCORE)
    S2.pack()
    Q = Label(root, font=FONT_SCORE, text="What is this?")
    
    #IMAGE
    canvas = Canvas(root,width="128",height="128")
    canvas.pack()
    Q.pack()

    photoApple = PhotoImage(file="apple.png")
    imgApple = Label(root, anchor="s", image=photoApple)
    imgApple.image = photoApple
    imgApple.place(x=280, y=100)
    #pilImage = Image.open("/home/pi/mu_code/buddy/apple.png")
    #image = ImageTk.PhotoImage(pilImage)
    #imagesprite = canvas.create_image(60, 70,image=imgApple)

    #T = Text(root, height=2, width=30)
    #T.pack()
    #T.insert(END, "Her skal det være bilde av en banan.")
    
    #def changeImage(imagePath):
     #   pilimage2 = Image.open(imagePath)
      #  image2 = ImageTk.PhotoImage(pilimage2)
       # imagesprite2 = BuddyQuiz.canvas.create_image(60, 70, image=image)

    
    def checkAnswer(self, ans):
        if ans == "eple":
            print("RIKTIG!")
            if BuddyQuiz.playerString == "PLAYER 1":
                BuddyQuiz.p1score += 10
                os.system('mpg321 /home/pi/mu_code/buddy/correct.mp3 &')
            elif BuddyQuiz.playerString == "PLAYER 2":
                os.system('mpg321 /home/pi/mu_code/buddy/correct.mp3 &')
                BuddyQuiz.p2score += 10
        else:
            os.system('mpg321 /home/pi/mu_code/buddy/wrong.mp3 &')
            print("Feil svar!")
            
        if BuddyQuiz.playerString == "PLAYER 1":
            BuddyQuiz.playerString = "PLAYER 2"
            BuddyQuiz.L.config(text="PLAYER 2")
            BuddyQuiz.L.config(fg="red")
            BuddyQuiz.S1.config(text="Player 1 Score: " + str(BuddyQuiz.p1score))
            BuddyQuiz.S2.config(text="Player 2 Score: " + str(BuddyQuiz.p2score))
        elif BuddyQuiz.playerString == "PLAYER 2":
            BuddyQuiz.playerString = "PLAYER 1"
            BuddyQuiz.L.config(text="PLAYER 1")
            BuddyQuiz.L.config(fg="blue")
            BuddyQuiz.S1.config(text="Player 1 Score: " + str(BuddyQuiz.p1score))
            BuddyQuiz.S2.config(text="Player 2 Score: " + str(BuddyQuiz.p2score))


bq = BuddyQuiz()
answerButton1 = Button(bq.root, font=bq.FONT_BUTTONS, text="banan", command=lambda: bq.checkAnswer("banan"))
answerButton2 = Button(bq.root, font=bq.FONT_BUTTONS, text="eple", command=lambda: bq.checkAnswer("eple"))
answerButton3 = Button(bq.root, font=bq.FONT_BUTTONS, text="potet", command=lambda: bq.checkAnswer("potet"))
answerButton4 = Button(bq.root, font=bq.FONT_BUTTONS, text="jordbær", command=lambda: bq.checkAnswer("jordbær"))
answerButton1.pack(side=LEFT, ipadx=50, ipady=25)
answerButton2.pack(side=LEFT, ipadx=50, ipady=25)
answerButton3.pack(side=LEFT, ipadx=50, ipady=25)
answerButton4.pack(side=LEFT, ipadx=50, ipady=25)
    
mainloop()