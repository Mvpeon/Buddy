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

        for F in (Meny, SpillMeny, Snakk, MemorySpill, LoadingScreen, Quiz, SnakkNybegynner):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry("800x480")
        self.show_frame(LoadingScreen)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit(self):
        exit()


class LoadingScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoLoading = tk.PhotoImage(file="loading.png")
        imgLoading = tk.Label(self, anchor="s", image=photoLoading)
        imgLoading.image = photoLoading

        button1 = tk.Button(self, text="MENY", command=lambda: controller.show_frame(Meny))
        button1.configure(image=photoLoading, bg='white', width="800", height="480")
        button1.pack()

class Meny(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoKom = tk.PhotoImage(file="kommknapp.png")
        photoLaer = tk.PhotoImage(file="laerknapp.png")
        photoSpill = tk.PhotoImage(file="spillknapp.png")

        imgKom = tk.Label(self, anchor="s", image=photoKom)
        imgLaer = tk.Label(self, anchor="s", image=photoLaer)
        imgSpill = tk.Label(self, anchor="s", image=photoSpill)

        imgKom.image = photoKom
        imgLaer.image = photoLaer
        imgSpill.image = photoSpill

        labelTittel = tk.Label(self, text="MENY", font=LARGE_FONT)
        buttonKom = tk.Button(self, image=photoKom, command=lambda: controller.show_frame(Snakk))
        buttonLær = tk.Button(self, image=photoLaer, command=lambda: controller.show_frame(Meny))
        buttonSpill = tk.Button(self, image=photoSpill, command=lambda: controller.show_frame(SpillMeny))

        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=10)

        buttonKom.place(x=110, y=150)
        buttonLær.place(x=310, y=150)
        buttonSpill.place(x=510, y=150)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)

        photoExit = tk.PhotoImage(file="exit.png")
        imgExit = tk.Label(self, anchor="s", image=photoExit)
        imgExit.image = photoExit
        buttonExit = tk.Button(self, image=photoExit, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: quit())
        buttonExit.place(x=10, y=10)

class Fagvelger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoNorsk = tk.PhotoImage(file="toad.png")
        photoSamfunnsfag = tk.PhotoImage(file="toad.png")
        photoNaturfag = tk.PhotoImage(file="toad.png")

        imgLaer = tk.Label(self, anchor="s", image=photoNorsk)
        imgSpill = tk.Label(self, anchor="s", image=photoSamfunnsfag)
        imgKom = tk.Label(self, anchor="s", image=photoNaturfag)

        imgKom.image = photoNorsk
        imgLaer.image = photoSamfunnsfag
        imgSpill.image = photoNaturfag

        labelTittel = tk.Label(self, text="VELG FAG", font=LARGE_FONT)
        buttonNorsk = tk.Button(self, image=photoNaturfag, command=lambda: controller.show_frame(Fagvelger))
        buttonSamfunnsfag = tk.Button(self, image=photoNaturfag, command=lambda: controller.show_frame(Fagvelger))
        buttonNaturfag = tk.Button(self, image=photoNaturfag, command=lambda: controller.show_frame(Fagvelger))

        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=10)

        buttonNorsk.place(x=110, y=150)
        buttonSamfunnsfag.place(x=310, y=150)
        buttonNaturfag.place(x=510, y=150)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0,
                                 command=lambda: controller.show_frame(Meny))
        buttonReturn.place(x=10, y=10)

class SpillMeny(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="SPILL", font=LARGE_FONT)
        labelTittel.configure(background="white")
        labelTittel.pack(pady=10, padx=5)

        photoMemory = tk.PhotoImage(file="memorytile.png")
        imgMemory = tk.Label(self, anchor="w", image=photoMemory)
        imgMemory.image = photoMemory
        buttonMemory = tk.Button(self, command=lambda: controller.show_frame(MemorySpill))
        buttonMemory.config(image=photoMemory)
        buttonMemory.place(x=70, y=120, width=300, height=300)

        photoQuiz = tk.PhotoImage(file="quiz.png")
        imgQuiz = tk.Label(self, anchor="w", image=photoQuiz)
        imgQuiz.image = photoQuiz
        buttonQuiz = tk.Button(self, command=lambda: controller.show_frame(Quiz))
        buttonQuiz.config(image=photoQuiz)
        buttonQuiz.place(x=430, y=120, width=300, height=300)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0,  activebackground="white",
                                 command=lambda: controller.show_frame(Meny))
        buttonReturn.place(x=10, y=10)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)

class MemorySpill(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, activebackground="white",
                                 borderwidth=0, command=lambda: controller.show_frame(SpillMeny))
        buttonReturn.place(x=10, y=10)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)

        from MemGameImg import MemGame
        x = MemGame(self)
        x.place(x=200, y=70)

        #photoReturn = tk.PhotoImage(file="restartikon.png")
        #imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        #imgReturn.image = photoReturn
        #buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0,
        #                         command=lambda: c.mainloop())
        #buttonReturn.place(x=720, y=400)

class Quiz(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(SpillMeny))
        buttonReturn.place(x=10, y=10)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)

        self.configure(background="white")

        # quiz spill



class Snakk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        labelTittel = tk.Label(self, text="SNAKK", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)
        labelTittel.configure(background="white")

        labelVanskelighetsgrad = tk.Label(self, text="How good is your Norwegian?", font=MEDIUM_FONT)
        labelVanskelighetsgrad.place(x=250, y=100)
        labelVanskelighetsgrad.config(bg="white")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Meny))
        buttonReturn.place(x=10, y=10)

        heter_sound = pygame.mixer.Sound("heter.wav")
        spille_sound = pygame.mixer.Sound("spille.wav")

        photoNorsk = tk.PhotoImage(file="toad.png")
        photoSamfunnsfag = tk.PhotoImage(file="toad.png")
        photoNaturfag = tk.PhotoImage(file="toad.png")

        imgLaer = tk.Label(self, anchor="s", image=photoNorsk)
        imgSpill = tk.Label(self, anchor="s", image=photoSamfunnsfag)
        imgKom = tk.Label(self, anchor="s", image=photoNaturfag)

        imgKom.image = photoNorsk
        imgLaer.image = photoSamfunnsfag
        imgSpill.image = photoNaturfag

        buttonA = tk.Button(self, text="Not good", command=lambda: controller.show_frame(SnakkNybegynner))
        buttonB = tk.Button(self, text="Okay", command=lambda: controller.show_frame(SnakkNybegynner))
        buttonC = tk.Button(self, text="Good", command=lambda: controller.show_frame(SnakkNybegynner))

        buttonA.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonB.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonC.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')

        buttonA.place(x=275, y=150)
        buttonB.place(x=275, y=230)
        buttonC.place(x=275, y=310)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)



        def heter():
            pygame.mixer.Sound.play(heter_sound)
            pygame.mixer.music.stop()

        def spille():
            pygame.mixer.Sound.play(spille_sound)
            pygame.mixer.music.stop()

class SnakkNybegynner(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photoReturn = tk.PhotoImage(file="returnknapp.png")
        imgReturn = tk.Label(self, anchor="s", image=photoReturn)
        imgReturn.image = photoReturn
        buttonReturn = tk.Button(self, image=photoReturn, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Snakk))
        buttonReturn.place(x=10, y=10)

        photoWifi = tk.PhotoImage(file="wifi.png")
        imgWifi = tk.Label(self, anchor="s", image=photoWifi)
        imgWifi.image = photoWifi  # keep a reference!
        imgWifi.config(background="white")
        imgWifi.place(x=740, y=5)

        labelTittel = tk.Label(self, text="SNAKK", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)
        labelTittel.configure(background="white")

        labelVanskelighetsgrad = tk.Label(self, text="Repeat after me.", font=MEDIUM_FONT)
        labelVanskelighetsgrad.place(x=320, y=100)
        labelVanskelighetsgrad.config(bg="white")

        photoIllustrasjon = tk.PhotoImage(file="toad.png")
        imgIllustrasjon = tk.Label(self, anchor="s", image=photoIllustrasjon)
        imgIllustrasjon.image = photoIllustrasjon
        imgIllustrasjon.place(x=330, y=150)

        hei_sound = pygame.mixer.Sound("hei.wav")
        buttonHei = tk.Button(self, text="Hei", command=lambda: hei())
        buttonHei.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonHei.place(x=275, y=350)

        def hei():
            pygame.mixer.Sound.play(hei_sound)
            pygame.mixer.music.stop()

app = BuddyOS()
app.mainloop()
