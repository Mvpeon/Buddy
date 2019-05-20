import tkinter as tk
#import MemoryGame
import pygame
pygame.init()

LARGE_FONT = ("Verdana", 22)
MEDIUM_FONT = ("Verdana", 14)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MG, Kommuniser, MG1, LoadingScreen):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry("800x480")
        self.show_frame(LoadingScreen)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoadingScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photoLoading = tk.PhotoImage(file="loading.png")
        imgLoading = tk.Label(self, anchor="s", image=photoLoading)
        imgLoading.image = photoLoading

        button1 = tk.Button(self, text="MENY", command=lambda: controller.show_frame(StartPage))
        button1.configure(image=photoLoading, bg='white', width="800", height="480")
        button1.pack()

        self.configure(background="white")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelTittel = tk.Label(self, text="MENY", font=LARGE_FONT)
        buttonKom = tk.Button(self, text="KOMMUNISER", command=lambda: controller.show_frame(Kommuniser))
        buttonLær = tk.Button(self, text="LÆR DEG", command=lambda: controller.show_frame(StartPage))
        buttonSpill = tk.Button(self, text="SPILL", command=lambda: controller.show_frame(MG))

        labelTittel.configure(background="white")
        buttonKom.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonLær.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonSpill.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')

        labelTittel.pack(pady=10, padx=10)
        buttonKom.pack(padx=5, pady=5)
        buttonLær.pack(padx=5, pady=5)
        buttonSpill.pack(padx=5, pady=5)

        self.configure(background="white")


class MG(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelTittel = tk.Label(self, text="SPILL", font=LARGE_FONT)

        photoMario = tk.PhotoImage(file="mario.png")
        photoLuigi = tk.PhotoImage(file="luigi.png")
        photoToad = tk.PhotoImage(file="toad.png")

        imgMario = tk.Label(self, anchor="s", image=photoMario)
        imgLuigi = tk.Label(self, anchor="w", image=photoLuigi)
        imgToad = tk.Label(self, anchor="w", image=photoToad)

        imgMario.image = photoMario  # keep a reference!
        imgLuigi.image = photoLuigi
        imgToad.image = photoToad

        buttonMeny = tk.Button(self, command=lambda: controller.show_frame(StartPage))
        luigi = tk.Button(self, command=lambda: controller.show_frame(MG1))
        toad = tk.Button(self, command=lambda: controller.show_frame(MG))

        labelTittel.configure(background="white")
        buttonMeny.configure(background='orange', height=2, width=20, fg='white', text="MENY", font="FONT_MEDIUM")
        luigi.config(image=photoLuigi)
        toad.config(image=photoToad)
        imgMario.config(background="white")

        labelTittel.pack(pady=10, padx=5)
        buttonMeny.pack(padx=5, pady=5)
        luigi.place(x=100, y=200, width=128, height=128)
        toad.place(x=600, y=200, width=128, height=128)
        imgMario.place(x=300, y=160)

        self.configure(background="white")


class MG1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="MENY", font=MEDIUM_FONT, command=lambda: controller.show_frame(StartPage))

        button1.configure(background='orange', height=2, width=20, fg='white')

        button1.pack()

        #import MemoryGame

        self.configure(background="white")

        #MemoryGame.canvas.pack()

class Kommuniser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelTittel = tk.Label(self, text="KOMMUNISER", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="MENY", font=MEDIUM_FONT, command=lambda: controller.show_frame(StartPage))

        labelTittel.configure(background="white")
        button1.configure(background='orange', height=2, width=20, fg='white')

        button1.pack(pady=5)

        self.configure(background="white")

        hei_sound = pygame.mixer.Sound("hei.wav")
        heter_sound = pygame.mixer.Sound("heter.wav")
        spille_sound = pygame.mixer.Sound("spille.wav")

        buttonA = tk.Button(self, text="Introduser meg", command=lambda: hei())
        buttonB = tk.Button(self, text="Hva heter du?", command=lambda: heter())
        buttonC = tk.Button(self, text="Spille ett spill?", command=lambda: spille())

        buttonA.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonB.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')
        buttonC.configure(background='purple', font=MEDIUM_FONT, height=2, width=20, fg='white')

        buttonA.pack(pady=5)
        buttonB.pack(pady=5)
        buttonC.pack(pady=5)

        def hei():
            pygame.mixer.Sound.play(hei_sound)
            pygame.mixer.music.stop()

        def heter():
            pygame.mixer.Sound.play(heter_sound)
            pygame.mixer.music.stop()

        def spille():
            pygame.mixer.Sound.play(spille_sound)
            pygame.mixer.music.stop()

app = SeaofBTCapp()
app.mainloop()