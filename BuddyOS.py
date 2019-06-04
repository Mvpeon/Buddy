import tkinter as tk
import pygame
pygame.init()

LARGE_FONT = ("Verdana", 22)
MEDIUM_FONT = ("Verdana", 14)

class BuddyOS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Language, Meny, SpillMeny, Translate, MemoryP1, MemoryP2, MemoryMeny, Quiz, Norsk, Fagvelger):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry("800x480")
        self.show_frame(Language)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit(self):
        exit()

class Meny(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoKom = tk.PhotoImage(file="talkbtn.png")
        photoLaer = tk.PhotoImage(file="learnbtn.png")
        photoSpill = tk.PhotoImage(file="gamesbtn.png")

        imgKom = tk.Label(self, anchor="s", image=photoKom)
        imgLaer = tk.Label(self, anchor="s", image=photoLaer)
        imgSpill = tk.Label(self, anchor="s", image=photoSpill)

        imgKom.image = photoKom
        imgLaer.image = photoLaer
        imgSpill.image = photoSpill

        labelTittel = tk.Label(self, text="MENU", font=LARGE_FONT)
        buttonKom = tk.Button(self, image=photoKom, highlightthickness=0, bg="white",
                              borderwidth=0, activebackground="white",
                              command=lambda: controller.show_frame(Translate))
        buttonLær = tk.Button(self, image=photoLaer, highlightthickness=0, bg="white",
                              borderwidth=0, activebackground="white",
                              command=lambda: controller.show_frame(Fagvelger))
        buttonSpill = tk.Button(self, image=photoSpill, highlightthickness=0, bg="white",
                                borderwidth=0, activebackground="white",
                                command=lambda: controller.show_frame(SpillMeny))

        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=10)

        labelLearn = tk.Label(self, text="Learn", bg="white", font=LARGE_FONT)
        labelTranslate = tk.Label(self, text="Translate", bg="white", font=LARGE_FONT)
        labelGames = tk.Label(self, text="Games", bg="white", font=LARGE_FONT)
        labelLearn.place(x=110, y=370)
        labelTranslate.place(x=325, y=370)
        labelGames.place(x=600, y=370)

        buttonLær.place(x=50, y=150)
        buttonKom.place(x=300, y=150)
        buttonSpill.place(x=550, y=150)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        photoExit = tk.PhotoImage(file="exit.png")
        imgExit = tk.Label(self, anchor="s", image=photoExit)
        imgExit.image = photoExit
        buttonExit = tk.Button(self, image=photoExit, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: quit())
        buttonExit.place(x=10, y=420)

class Language(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoGB = tk.PhotoImage(file="GB.png")
        photoSpain = tk.PhotoImage(file="Spain.png")
        photoFrance = tk.PhotoImage(file="France.png")
        photoSyria = tk.PhotoImage(file="Syria.png")

        imgGB = tk.Label(self, anchor="s", image=photoGB)
        imgSpain = tk.Label(self, anchor="s", image=photoSpain)
        imgFrance = tk.Label(self, anchor="s", image=photoFrance)
        imgSyria = tk.Label(self, anchor="s", image=photoSyria)

        imgGB.image = photoGB
        imgSpain.image = photoSpain
        imgFrance.image = photoFrance
        imgSyria.image = photoSyria

        labelTittel = tk.Label(self, text="CHOOSE A LANGUAGE", font=LARGE_FONT)
        buttonGB = tk.Button(self, image=photoGB, highlightthickness=0, borderwidth=0, activebackground="white", command=lambda: controller.show_frame(Meny))
        buttonSpain = tk.Button(self, image=photoSpain, highlightthickness=0, borderwidth=0, activebackground="white", command=lambda: controller.show_frame(Language))
        buttonFrance = tk.Button(self, image=photoFrance, highlightthickness=0, borderwidth=0, activebackground="white", command=lambda: controller.show_frame(Language))
        buttonSyria = tk.Button(self, image=photoSyria, highlightthickness=0, borderwidth=0, activebackground="white", command=lambda: controller.show_frame(Language))

        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=10)

        buttonGB.place(x=100, y=80)
        buttonSpain.place(x=100, y=280)
        buttonFrance.place(x=430, y=80)
        buttonSyria.place(x=430, y=280)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

class Fagvelger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoNorsk = tk.PhotoImage(file="greeting.png")
        photoNaturfag = tk.PhotoImage(file="wat.png")

        imgNorsk = tk.Label(self, anchor="s", image=photoNorsk)
        imgNaturfag = tk.Label(self, anchor="s", image=photoNaturfag)

        imgNorsk.image = photoNorsk
        imgNaturfag.image = photoNaturfag

        labelTittel = tk.Label(self, text="CHOOSE SUBJECT", font=LARGE_FONT, bg="white")
        labelTittel.pack(pady=10)

        labelDev = tk.Label(self, text="(Under development)", font=MEDIUM_FONT, bg="white")
        labelDev.place(x=465, y=405)

        labelNorsk = tk.Label(self, text="Norwegian", font=LARGE_FONT, bg="white")
        labelNorsk.place(x=165, y=405)

        buttonNorsk = tk.Button(self, image=photoNorsk, highlightthickness=0, borderwidth=0, activebackground="white", command=lambda: controller.show_frame(Norsk))
        buttonNaturfag = tk.Button(self, image=photoNaturfag, highlightthickness=0, borderwidth=0, activebackground="white", command=lambda: controller.show_frame(Fagvelger))

        buttonNorsk.place(x=120, y=150)
        buttonNaturfag.place(x=470, y=180)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Meny))
        buttonReturn.place(x=10, y=10)

class SpillMeny(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="GAMES", font=LARGE_FONT)
        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=5)

        labelDev = tk.Label(self, text="(Under development)", font=MEDIUM_FONT)
        labelDev.configure(background="white")
        labelDev.place(x=445, y=370)

        labelMemGame = tk.Label(self, text="Memory Game", font=LARGE_FONT)
        labelMemGame.configure(background="white")
        labelMemGame.place(x=142, y=370)

        photoMemory = tk.PhotoImage(file="memorygame.png")
        imgMemory = tk.Label(self, anchor="w", image=photoMemory)
        imgMemory.image = photoMemory
        buttonMemory = tk.Button(self, command=lambda: controller.show_frame(MemoryMeny))
        buttonMemory.config(image=photoMemory, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonMemory.place(x=150, y=150, width=200, height=200)

        photoQuiz = tk.PhotoImage(file="wat.png")
        imgQuiz = tk.Label(self, anchor="w", image=photoQuiz)
        imgQuiz.image = photoQuiz
        buttonQuiz = tk.Button(self, command=lambda: controller.show_frame(SpillMeny))
        buttonQuiz.config(image=photoQuiz, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonQuiz.place(x=450, y=150, width=200, height=200)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0,  activebackground="white",
                                 command=lambda: controller.show_frame(Meny))
        buttonReturn.place(x=10, y=10)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)


class MemoryMeny(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="MEMORY GAME", font=LARGE_FONT)
        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=5)

        photoMemory = tk.PhotoImage(file="singleplayer.png")
        imgMemory = tk.Label(self, anchor="w", image=photoMemory)
        imgMemory.image = photoMemory
        buttonMemory = tk.Button(self, command=lambda: controller.show_frame(MemoryP1))
        buttonMemory.config(image=photoMemory, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonMemory.place(x=150, y=150, width=200, height=200)

        photoQuiz = tk.PhotoImage(file="multiplayer.png")
        imgQuiz = tk.Label(self, anchor="w", image=photoQuiz)
        imgQuiz.image = photoQuiz
        buttonQuiz = tk.Button(self, command=lambda: controller.show_frame(MemoryP2))
        buttonQuiz.config(image=photoQuiz, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonQuiz.place(x=450, y=150, width=200, height=200)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(SpillMeny))
        buttonReturn.place(x=10, y=10)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        label1P = tk.Label(self, text="Single Player", font=LARGE_FONT)
        label1P.configure(background="white")
        label1P.place(x=145, y=370)

        label2P = tk.Label(self, text="Two Players", font=LARGE_FONT)
        label2P.configure(background="white")
        label2P.place(x=460, y=370)

class MemoryP1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, activebackground="white",
                                 borderwidth=0, command=lambda: controller.show_frame(MemoryMeny))
        buttonReturn.place(x=10, y=10)

        from Memory1P import MemGame
        x = MemGame(self)
        x.place(x=125, y=20)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

class MemoryP2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, activebackground="white",
                                 borderwidth=0, command=lambda: controller.show_frame(SpillMeny))
        buttonReturn.place(x=10, y=10)

        from Memory2P import MemGame
        x = MemGame(self)
        x.place(x=125, y=20)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

class Translate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="TRANSLATE", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)
        labelTittel.configure(background="white")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Meny))
        buttonReturn.place(x=10, y=10)

        hei_sound = pygame.mixer.Sound("hei.wav")
        heter_sound = pygame.mixer.Sound("heter.wav")
        spille_sound = pygame.mixer.Sound("spille.wav")

        photoHello = tk.PhotoImage(file="hello.png")
        imgKnapp = tk.Label(self, anchor="s", image=photoHello)
        imgKnapp.image = photoHello  # keep a reference!
        imgKnapp.config(background="white")

        photoName = tk.PhotoImage(file="name.png")
        imgName = tk.Label(self, anchor="s", image=photoName)
        imgName.image = photoName  # keep a reference!
        imgName.config(background="white")

        photoGame = tk.PhotoImage(file="game.png")
        imgGame = tk.Label(self, anchor="s", image=photoGame)
        imgGame.image = photoGame  # keep a reference!
        imgGame.config(background="white")

        buttonB = tk.Button(self, image=photoHello, highlightthickness=0, borderwidth=0, activebackground="white", text="Hei, jeg heter buddy!", command=lambda: hei())
        buttonA = tk.Button(self, image=photoName, highlightthickness=0, borderwidth=0, activebackground="white", text="Hva heter du?", command=lambda: heter())
        buttonC = tk.Button(self, image=photoGame, highlightthickness=0, borderwidth=0, activebackground="white", text="Vil du spille et spill?", command=lambda: spille())

        buttonA.configure(background='white', font=MEDIUM_FONT, fg='white') #height=2, width=20,
        buttonB.configure(background='white', font=MEDIUM_FONT, fg='white')
        buttonC.configure(background='white', font=MEDIUM_FONT, fg='white')

        buttonB.place(x=210, y=140)
        buttonA.place(x=210, y=240)
        buttonC.place(x=210, y=340)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        def heter():
            pygame.mixer.Sound.play(heter_sound)
            pygame.mixer.music.stop()

        def spille():
            pygame.mixer.Sound.play(spille_sound)
            pygame.mixer.music.stop()

        def hei():
            pygame.mixer.Sound.play(hei_sound)
            pygame.mixer.music.stop()

class Norsk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        correct_sound = pygame.mixer.Sound("correct.wav")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Fagvelger))
        buttonReturn.place(x=10, y=10)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        labelTittel = tk.Label(self, text="NORWEGIAN", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)
        labelTittel.configure(background="white")

        labelHi = tk.Label(self, text="English: Hi, my name is... \nNorwegian: Hei, jeg heter...", font=MEDIUM_FONT)
        labelHi.place(x=260, y=55)
        labelHi.config(bg="white")

        photoIllustrasjon = tk.PhotoImage(file="greeting.png")
        imgIllustrasjon = tk.Label(self, anchor="s", image=photoIllustrasjon, highlightthickness=0, borderwidth=0)
        imgIllustrasjon.image = photoIllustrasjon
        imgIllustrasjon.place(x=273, y=120)

        hei_sound = pygame.mixer.Sound("heijegheter.wav")

        photoKnapp = tk.PhotoImage(file="repeat.png")
        imgKnapp = tk.Label(self, anchor="s", image=photoKnapp)
        imgKnapp.image = photoKnapp
        imgKnapp.config(background="white")

        buttonRepeat = tk.Button(self, image=photoKnapp, highlightthickness=0, borderwidth=0, activebackground="white",
                            text="Hei, jeg heter buddy!", command=lambda: hei())
        buttonRepeat.place(x=200, y=380)

        def hei():
            pygame.mixer.Sound.play(hei_sound)
            pygame.mixer.music.stop()
            self.after(4000, correct)

        def correct():
            pygame.mixer.Sound.play(correct_sound)
            pygame.mixer.music.stop()

class Quiz(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(SpillMeny))
        buttonReturn.place(x=10, y=10)

        photoBatteri = tk.PhotoImage(file="batteri.png")
        imgBatteri = tk.Label(self, anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        self.configure(background="white")

        # quiz spill

app = BuddyOS()
app.mainloop()
