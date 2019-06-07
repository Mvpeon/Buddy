import tkinter as tk
import pygame
pygame.init()

LARGE_FONT = ("Verdana", 22)
MEDIUM_FONT = ("Verdana", 14)
SMALL_FONT = ("Verdana", 10)

BeenToSubjects = False
BeenToMenu = False
BeenBackToMenu = False
BeenToMemoryMenu = False

class BuddyOS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Language, Menu, Games, Translate, MemoryP1, MemoryP2, MemoryMenu, Norwegian, Subjects, Common):
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


class Common(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photoBatteri = tk.PhotoImage(file="Ressurser/GUI elementer/batteri.png")
        imgBatteri = tk.Label(anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoBatteri = tk.PhotoImage(file="Ressurser/GUI elementer/batteri.png")
        imgBatteri = tk.Label(anchor="s", image=photoBatteri)
        imgBatteri.image = photoBatteri  # keep a reference!
        imgBatteri.config(background="white")
        imgBatteri.place(x=710, y=15)

        subjects_sound = pygame.mixer.Sound("Ressurser/Lyd/subjects.wav")

        photoKom = tk.PhotoImage(file="Ressurser/GUI elementer/talkbtn.png")
        photoLaer = tk.PhotoImage(file="Ressurser/GUI elementer/learnbtn.png")
        photoSpill = tk.PhotoImage(file="Ressurser/GUI elementer/gamesbtn.png")

        imgKom = tk.Label(self, anchor="s", image=photoKom)
        imgLaer = tk.Label(self, anchor="s", image=photoLaer)
        imgSpill = tk.Label(self, anchor="s", image=photoSpill)

        imgKom.image = photoKom
        imgLaer.image = photoLaer
        imgSpill.image = photoSpill

        labelTittel = tk.Label(self, text="MENU", font=LARGE_FONT)
        buttonTranslate = tk.Button(self, image=photoKom, highlightthickness=0, bg="white",
                              borderwidth=0, activebackground="white",
                              command=lambda: goTranslate())
        buttonSubjects = tk.Button(self, image=photoLaer, highlightthickness=0, bg="white",
                              borderwidth=0, activebackground="white",
                              command=lambda: goSubjects())
        buttonGames = tk.Button(self, image=photoSpill, highlightthickness=0, bg="white",
                                borderwidth=0, activebackground="white",
                                command=lambda: goGames())

        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=10)

        labelLearn = tk.Label(self, text="Learn", bg="white", font=LARGE_FONT)
        labelTranslate = tk.Label(self, text="Translate", bg="white", font=LARGE_FONT)
        labelGames = tk.Label(self, text="Games", bg="white", font=LARGE_FONT)
        labelLearn.place(x=110, y=370)
        labelTranslate.place(x=325, y=370)
        labelGames.place(x=600, y=370)

        buttonSubjects.place(x=50, y=150)
        buttonTranslate.place(x=300, y=150)
        buttonGames.place(x=550, y=150)

        photoExit = tk.PhotoImage(file="Ressurser/GUI elementer/exit.png")
        imgExit = tk.Label(self, anchor="s", image=photoExit)
        imgExit.image = photoExit
        buttonExit = tk.Button(self, image=photoExit, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: quit())
        buttonExit.place(x=80, y=15)

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Language))
        buttonReturn.place(x=10, y=10)

        def goSubjects():
            global BeenToSubjects
            if (BeenToSubjects == False):
                pygame.mixer.stop()
                pygame.mixer.Sound.play(subjects_sound)
                BeenToSubjects = True
            controller.show_frame(Subjects)

        def goTranslate():
            #pygame.mixer.Sound.play(translate_sound)
            #pygame.mixer.music.stop()
            controller.show_frame(Translate)

        def goGames():
            #pygame.mixer.Sound.play(games_sound)
            #pygame.mixer.music.stop()
            controller.show_frame(Games)

class Language(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        buddy_sound = pygame.mixer.Sound("Ressurser/Lyd/hibuddy.wav")

        photoGB = tk.PhotoImage(file="Ressurser/GUI elementer/GB.png")
        photoSpain = tk.PhotoImage(file="Ressurser/GUI elementer/Spain.png")
        photoFrance = tk.PhotoImage(file="Ressurser/GUI elementer/France.png")
        photoSyria = tk.PhotoImage(file="Ressurser/GUI elementer/Syria.png")

        imgGB = tk.Label(self, anchor="s", image=photoGB)
        imgSpain = tk.Label(self, anchor="s", image=photoSpain)
        imgFrance = tk.Label(self, anchor="s", image=photoFrance)
        imgSyria = tk.Label(self, anchor="s", image=photoSyria)

        imgGB.image = photoGB
        imgSpain.image = photoSpain
        imgFrance.image = photoFrance
        imgSyria.image = photoSyria

        buttonGB = tk.Button(self, image=photoGB, highlightthickness=0, borderwidth=0, activebackground="white",
                             command=lambda: goMenu())
        buttonSpain = tk.Button(self, image=photoSpain, highlightthickness=0, borderwidth=0, activebackground="white",
                                command=lambda: controller.show_frame(Language))
        buttonFrance = tk.Button(self, image=photoFrance, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Language))
        buttonSyria = tk.Button(self, image=photoSyria, highlightthickness=0, borderwidth=0, activebackground="white",
                                command=lambda: controller.show_frame(Language))

        #labelTittel = tk.Label(self, text="CHOOSE A LANGUAGE", font=LARGE_FONT)
        #labelTittel.configure(background="white")
        #labelTittel.pack(pady=10, padx=10)

        labelGB = tk.Label(self, text="United Kingdom", font=LARGE_FONT, bg="white")
        labelGB.place(x=108, y=180)
        labelSpain = tk.Label(self, text="España", font=LARGE_FONT, bg="white")
        labelSpain.place(x=170, y=418)
        labelFrance = tk.Label(self, text="France", font=LARGE_FONT, bg="white")
        labelFrance.place(x=505, y=180)
        labelSyria = tk.Label(self, text="سوريا", font=LARGE_FONT, bg="white",)
        labelSyria.place(x=520, y=418)

        labelDevelopment1 = tk.Label(self, text="Under Development", font=SMALL_FONT, bg="white")
        labelDevelopment1.place(x=490, y=455)
        labelDevelopment2 = tk.Label(self, text="Under Development", font=SMALL_FONT, bg="white")
        labelDevelopment2.place(x=490, y=215)
        labelDevelopment3 = tk.Label(self, text="Under Development", font=SMALL_FONT, bg="white")
        labelDevelopment3.place(x=155, y=455)

        buttonGB.place(x=100, y=10)
        buttonSpain.place(x=100, y=250)
        buttonFrance.place(x=430, y=10)
        buttonSyria.place(x=430, y=250)

        def goMenu():
            global BeenToMenu
            if (BeenToMenu == False):
                pygame.mixer.stop()
                pygame.mixer.Sound.play(buddy_sound)
                BeenToMenu = True
            controller.show_frame(Menu)


class Subjects(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoNorsk = tk.PhotoImage(file="Ressurser/GUI elementer/buddynorwegian.png")
        photoNaturfag = tk.PhotoImage(file="Ressurser/GUI elementer/wut.png")

        imgNorsk = tk.Label(self, anchor="s", image=photoNorsk, bg="black")
        imgNaturfag = tk.Label(self, anchor="s", image=photoNaturfag)

        imgNorsk.image = photoNorsk
        imgNaturfag.image = photoNaturfag

        labelTittel = tk.Label(self, text="CHOOSE SUBJECT", font=LARGE_FONT, bg="white")
        labelTittel.pack(pady=10)

        labelDev = tk.Label(self, text="(Under development)", font=MEDIUM_FONT, bg="white")
        labelDev.place(x=465, y=402)

        labelNorsk = tk.Label(self, text="Norwegian", font=LARGE_FONT, bg="white")
        labelNorsk.place(x=130, y=395)

        buttonNorsk = tk.Button(self, image=photoNorsk, highlightthickness=0, borderwidth=0, activebackground="white", bg="white",
                                command=lambda: controller.show_frame(Norwegian))
        buttonNaturfag = tk.Button(self, image=photoNaturfag, highlightthickness=0, borderwidth=0, activebackground="white",
                                   command=lambda: controller.show_frame(Subjects))

        buttonNorsk.place(x=120, y=120)
        buttonNaturfag.place(x=470, y=180)

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: returnToMenu())
        buttonReturn.place(x=10, y=10)

        menu_sound = pygame.mixer.Sound("Ressurser/Lyd/menu.wav")

        def returnToMenu():
            global BeenBackToMenu
            if (BeenBackToMenu == False):
                pygame.mixer.stop()
                pygame.mixer.Sound.play(menu_sound)
                BeenBackToMenu = True
            controller.show_frame(Menu)


class Games(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="GAMES", font=LARGE_FONT)
        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=5)

        labelDev = tk.Label(self, text="(Under development)", font=MEDIUM_FONT)
        labelDev.configure(background="white")
        labelDev.place(x=445, y=377)

        labelMemGame = tk.Label(self, text="Memory Game", font=LARGE_FONT)
        labelMemGame.configure(background="white")
        labelMemGame.place(x=142, y=370)

        photoMemory = tk.PhotoImage(file="Ressurser/GUI elementer/memorygame.png")
        imgMemory = tk.Label(self, anchor="w", image=photoMemory)
        imgMemory.image = photoMemory
        buttonMemory = tk.Button(self, command=lambda: goMemory())
        buttonMemory.config(image=photoMemory, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonMemory.place(x=150, y=150, width=200, height=200)

        photoWhat = tk.PhotoImage(file="Ressurser/GUI elementer/wut.png")
        imgWhat = tk.Label(self, anchor="w", image=photoWhat)
        imgWhat.image = photoWhat
        buttonWhat = tk.Button(self, command=lambda: controller.show_frame(Games))
        buttonWhat.config(image=photoWhat, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonWhat.place(x=450, y=150, width=200, height=200)

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0,  activebackground="white",
                                 command=lambda: returnToMenu())
        buttonReturn.place(x=10, y=10)

        menu_sound = pygame.mixer.Sound("Ressurser/Lyd/menu.wav")
        memory_sound = pygame.mixer.Sound("Ressurser/Lyd/playingwith.wav")

        def returnToMenu():
            global BeenBackToMenu
            if (BeenBackToMenu == False):
                pygame.mixer.stop()
                pygame.mixer.Sound.play(menu_sound)
                BeenBackToMenu = True
            controller.show_frame(Menu)

        def goMemory():
            global BeenToMemoryMenu
            if (BeenToMemoryMenu == False):
                pygame.mixer.stop()
                pygame.mixer.Sound.play(memory_sound)
                BeenToMemoryMenu = True
            controller.show_frame(MemoryMenu)


class MemoryMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="MEMORY GAME", font=LARGE_FONT)
        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=5)

        photoMemory = tk.PhotoImage(file="Ressurser/GUI elementer/singleplayer.png")
        imgMemory = tk.Label(self, anchor="w", image=photoMemory)
        imgMemory.image = photoMemory
        buttonMemory = tk.Button(self, command=lambda: controller.show_frame(MemoryP1))
        buttonMemory.config(image=photoMemory, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonMemory.place(x=150, y=150, width=200, height=200)

        photoWhat = tk.PhotoImage(file="Ressurser/GUI elementer/multiplayer.png")
        imgWhat = tk.Label(self, anchor="w", image=photoWhat)
        imgWhat.image = photoWhat
        buttonWhat = tk.Button(self, command=lambda: controller.show_frame(MemoryP2))
        buttonWhat.config(image=photoWhat, background="white", highlightthickness=0, borderwidth=0, activebackground="white")
        buttonWhat.place(x=450, y=150, width=200, height=200)

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Games))
        buttonReturn.place(x=10, y=10)

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

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, activebackground="white",
                                 borderwidth=0, command=lambda: controller.show_frame(MemoryMenu))
        buttonReturn.place(x=10, y=10)

        from Memory1P import MemGame
        x = MemGame(self)
        x.place(x=125, y=20)

class MemoryP2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, activebackground="white",
                                 borderwidth=0, command=lambda: controller.show_frame(Games))
        buttonReturn.place(x=10, y=10)

        from Memory2P import MemGame
        x = MemGame(self)
        x.place(x=125, y=20)

class Translate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="TRANSLATE", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)
        labelTittel.configure(background="white")

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: returnToMenu())
        buttonReturn.place(x=10, y=10)

        hei_sound = pygame.mixer.Sound("Ressurser/Lyd/hei.wav")
        heter_sound = pygame.mixer.Sound("Ressurser/Lyd/heter.wav")
        spille_sound = pygame.mixer.Sound("Ressurser/Lyd/spille.wav")

        photoHello = tk.PhotoImage(file="Ressurser/GUI elementer/hello.png")
        imgKnapp = tk.Label(self, anchor="s", image=photoHello)
        imgKnapp.image = photoHello  # keep a reference!
        imgKnapp.config(background="white")

        photoName = tk.PhotoImage(file="Ressurser/GUI elementer/name.png")
        imgName = tk.Label(self, anchor="s", image=photoName)
        imgName.image = photoName  # keep a reference!
        imgName.config(background="white")

        photoGame = tk.PhotoImage(file="Ressurser/GUI elementer/game.png")
        imgGame = tk.Label(self, anchor="s", image=photoGame)
        imgGame.image = photoGame  # keep a reference!
        imgGame.config(background="white")

        buttonB = tk.Button(self, image=photoHello, highlightthickness=0, borderwidth=0, activebackground="white", text="Hei, jeg heter buddy!",
                            command=lambda: hei())
        buttonA = tk.Button(self, image=photoName, highlightthickness=0, borderwidth=0, activebackground="white", text="Hva heter du?",
                            command=lambda: heter())
        buttonC = tk.Button(self, image=photoGame, highlightthickness=0, borderwidth=0, activebackground="white", text="Vil du spille et spill?",
                            command=lambda: spille())

        buttonA.configure(background='white', font=MEDIUM_FONT, fg='white') #height=2, width=20,
        buttonB.configure(background='white', font=MEDIUM_FONT, fg='white')
        buttonC.configure(background='white', font=MEDIUM_FONT, fg='white')

        buttonB.place(x=210, y=140)
        buttonA.place(x=210, y=240)
        buttonC.place(x=210, y=340)

        menu_sound = pygame.mixer.Sound("Ressurser/Lyd/menu.wav")

        def returnToMenu():
            global BeenBackToMenu
            if (BeenBackToMenu == False):
                pygame.mixer.stop()
                pygame.mixer.Sound.play(menu_sound)
                BeenBackToMenu = True
            controller.show_frame(Menu)

        def heter():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(heter_sound)

        def spille():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(spille_sound)

        def hei():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(hei_sound)

class Norwegian(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        correct_sound = pygame.mixer.Sound("Ressurser/Lyd/correct.wav")

        photoReturn = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Subjects))
        buttonReturn.place(x=10, y=10)

        labelTittel = tk.Label(self, text="NORWEGIAN", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)
        labelTittel.configure(background="white")

        labelHi = tk.Label(self, text="       English: Hi, my name is... \nNorwegian: Hei, jeg heter...", font=MEDIUM_FONT)
        labelHi.place(x=220, y=100)
        labelHi.config(bg="white")

        photoBuddy = tk.PhotoImage(file="Ressurser/GUI elementer/buddytalkingsmall.png")
        imgBuddy = tk.Label(self, anchor="s", image=photoBuddy, highlightthickness=0, borderwidth=0, bg="white")
        imgBuddy.image = photoBuddy
        imgBuddy.place(x=330, y=200)

        photoOrangeMan = tk.PhotoImage(file="Ressurser/GUI elementer/orangetalking.png")
        imgOrangeMan = tk.Label(self, anchor="s", image=photoOrangeMan, highlightthickness=0, borderwidth=0,
                                   bg="white")
        imgOrangeMan.image = photoOrangeMan
        imgOrangeMan.place(x=-200, y=200)

        hei_sound = pygame.mixer.Sound("Ressurser/Lyd/heijegheter.wav")

        photoKnapp = tk.PhotoImage(file="Ressurser/GUI elementer/repeat.png")
        imgKnapp = tk.Label(self, anchor="s", image=photoKnapp)
        imgKnapp.image = photoKnapp
        imgKnapp.config(background="white")

        buttonRepeat = tk.Button(self, image=photoKnapp, highlightthickness=0, borderwidth=0, activebackground="white",
                            text="Hei, jeg heter buddy!", bg="white", command=lambda: repeatAfterMe())
        buttonRepeat.place(x=200, y=390)

        def repeatAfterMe():
            hei()
            self.after(2000, showOrangeMan())
            self.after(3000, correct)

        def correct():
            pygame.mixer.Sound.play(correct_sound)

        def showOrangeMan():
            imgBuddy.place(x=-200, y=200)
            imgOrangeMan.place(x=330, y=200)

        def hei():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(hei_sound)

app = BuddyOS()
app.mainloop()