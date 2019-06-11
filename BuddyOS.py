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
OptionsIsOpen = False


class BuddyOS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.winfo_toplevel().title("Beep Boop")

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

        photo_batteri = tk.PhotoImage(file="Ressurser/GUI elementer/batteri.png")
        img_batteri = tk.Label(anchor="s", image=photo_batteri)
        img_batteri.image = photo_batteri
        img_batteri.config(background="white")
        img_batteri.place(x=670, y=15)

        photo_options = tk.PhotoImage(file="Ressurser/GUI elementer/innstillinger.png")
        img_options = tk.Label(anchor="s", image=photo_options)
        img_options.image = photo_options
        button_options = tk.Button(image=photo_options, highlightthickness=0, borderwidth=0, activebackground="white",
                                   bg="white", command=lambda: toggle_options())
        button_options.place(x=750, y=5)

        canvas = tk.Canvas(width=150, height=140, bg="white")
        label_exit = tk.Label(canvas, text="Exit Program", bg="white")
        label_exit.place(x=10, y=30)

        photo_exit = tk.PhotoImage(file="Ressurser/GUI elementer/exit.png")
        img_exit = tk.Label(canvas, anchor="s", image=photo_exit)
        img_exit.image = photo_exit
        button_exit = tk.Button(canvas, image=photo_exit, highlightthickness=0, borderwidth=0, activebackground="white",
                                command=lambda: quit())
        button_exit.place(x=90, y=15)

        photo_lyd = tk.PhotoImage(file="Ressurser/GUI elementer/lydpaa.png")
        img_lyd = tk.Label(canvas, anchor="s", image=photo_lyd)
        img_lyd.image = photo_lyd
        button_lyd = tk.Button(canvas, image=photo_lyd, highlightthickness=0, borderwidth=0, activebackground="white",
                               bg="white", command=lambda: None)
        button_lyd.place(x=95, y=95)

        label_mute = tk.Label(canvas, text="Mute Sound", bg="white")
        label_mute.place(x=10, y=100)

        def toggle_options():
            global OptionsIsOpen
            if not OptionsIsOpen:
                canvas.place(x=640, y=60)
                OptionsIsOpen = True
            else:
                canvas.place(x=800, y=0)
                OptionsIsOpen = False


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        subjects_sound = pygame.mixer.Sound("Ressurser/Lyd/subjects.wav")

        photo_kom = tk.PhotoImage(file="Ressurser/GUI elementer/talkbtn.png")
        photo_laer = tk.PhotoImage(file="Ressurser/GUI elementer/learnbtn.png")
        photo_spill = tk.PhotoImage(file="Ressurser/GUI elementer/gamesbtn.png")

        img_kom = tk.Label(self, anchor="s", image=photo_kom)
        img_laer = tk.Label(self, anchor="s", image=photo_laer)
        img_spill = tk.Label(self, anchor="s", image=photo_spill)

        img_kom.image = photo_kom
        img_laer.image = photo_laer
        img_spill.image = photo_spill

        label_tittel = tk.Label(self, text="MENU", font=LARGE_FONT)
        button_translate = tk.Button(self, image=photo_kom, highlightthickness=0, bg="white",
                                     borderwidth=0, activebackground="white",
                                     command=lambda: go_translate())
        button_subjects = tk.Button(self, image=photo_laer, highlightthickness=0, bg="white",
                                    borderwidth=0, activebackground="white",
                                    command=lambda: go_subjects())
        button_games = tk.Button(self, image=photo_spill, highlightthickness=0, bg="white",
                                 borderwidth=0, activebackground="white",
                                 command=lambda: go_games())

        label_tittel.configure(background="white")
        label_tittel.pack(pady=10, padx=10)

        label_learn = tk.Label(self, text="Learn", bg="white", font=LARGE_FONT)
        label_translate = tk.Label(self, text="Translate", bg="white", font=LARGE_FONT)
        label_games = tk.Label(self, text="Games", bg="white", font=LARGE_FONT)
        label_learn.place(x=110, y=370)
        label_translate.place(x=325, y=370)
        label_games.place(x=600, y=370)

        button_subjects.place(x=50, y=150)
        button_translate.place(x=300, y=150)
        button_games.place(x=550, y=150)

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: controller.show_frame(Language))
        button_return.place(x=10, y=10)

        def go_subjects():
            global BeenToSubjects
            if not BeenToSubjects:
                pygame.mixer.stop()
                pygame.mixer.Sound.play(subjects_sound)
                BeenToSubjects = True
            controller.show_frame(Subjects)

        def go_translate():
            controller.show_frame(Translate)

        def go_games():
            controller.show_frame(Games)


class Language(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        buddy_sound = pygame.mixer.Sound("Ressurser/Lyd/hibuddy.wav")

        photo_gb = tk.PhotoImage(file="Ressurser/GUI elementer/GB.png")
        photo_spain = tk.PhotoImage(file="Ressurser/GUI elementer/Spain.png")
        photo_france = tk.PhotoImage(file="Ressurser/GUI elementer/France.png")
        photo_syria = tk.PhotoImage(file="Ressurser/GUI elementer/Syria.png")

        img_gb = tk.Label(self, anchor="s", image=photo_gb)
        img_spain = tk.Label(self, anchor="s", image=photo_spain)
        img_france = tk.Label(self, anchor="s", image=photo_france)
        img_syria = tk.Label(self, anchor="s", image=photo_syria)

        img_gb.image = photo_gb
        img_spain.image = photo_spain
        img_france.image = photo_france
        img_syria.image = photo_syria

        button_gb = tk.Button(self, image=photo_gb, highlightthickness=0, borderwidth=0, activebackground="white",
                              command=lambda: go_menu())
        button_spain = tk.Button(self, image=photo_spain, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Language))
        button_france = tk.Button(self, image=photo_france, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: controller.show_frame(Language))
        button_syria = tk.Button(self, image=photo_syria, highlightthickness=0, borderwidth=0, activebackground="white",
                                 command=lambda: controller.show_frame(Language))

        label_gb = tk.Label(self, text="United Kingdom", font=LARGE_FONT, bg="white")
        label_gb.place(x=128, y=180)
        label_spain = tk.Label(self, text="España", font=LARGE_FONT, bg="white")
        label_spain.place(x=190, y=418)
        label_france = tk.Label(self, text="France", font=LARGE_FONT, bg="white")
        label_france.place(x=485, y=180)
        label_syria = tk.Label(self, text="سوريا", font=LARGE_FONT, bg="white", )
        label_syria.place(x=500, y=418)

        label_development1 = tk.Label(self, text="Under Development", font=SMALL_FONT, bg="white")
        label_development1.place(x=470, y=455)
        label_development2 = tk.Label(self, text="Under Development", font=SMALL_FONT, bg="white")
        label_development2.place(x=470, y=215)
        label_development3 = tk.Label(self, text="Under Development", font=SMALL_FONT, bg="white")
        label_development3.place(x=175, y=455)

        button_gb.place(x=120, y=10)
        button_spain.place(x=120, y=250)
        button_france.place(x=410, y=10)
        button_syria.place(x=410, y=250)

        def go_menu():
            global BeenToMenu
            if not BeenToMenu:
                pygame.mixer.stop()
                pygame.mixer.Sound.play(buddy_sound)
                BeenToMenu = True
            controller.show_frame(Menu)


class Subjects(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photo_norsk = tk.PhotoImage(file="Ressurser/GUI elementer/buddynorwegian.png")
        photo_naturfag = tk.PhotoImage(file="Ressurser/GUI elementer/wut.png")

        img_norsk = tk.Label(self, anchor="s", image=photo_norsk, bg="black")
        img_naturfag = tk.Label(self, anchor="s", image=photo_naturfag)

        img_norsk.image = photo_norsk
        img_naturfag.image = photo_naturfag

        label_tittel = tk.Label(self, text="CHOOSE SUBJECT", font=LARGE_FONT, bg="white")
        label_tittel.pack(pady=10)

        label_dev = tk.Label(self, text="(Under development)", font=MEDIUM_FONT, bg="white")
        label_dev.place(x=465, y=402)

        label_norsk = tk.Label(self, text="Norwegian", font=LARGE_FONT, bg="white")
        label_norsk.place(x=130, y=395)

        button_norsk = tk.Button(self, image=photo_norsk, highlightthickness=0, borderwidth=0, activebackground="white",
                                 bg="white",
                                 command=lambda: controller.show_frame(Norwegian))
        button_naturfag = tk.Button(self, image=photo_naturfag, highlightthickness=0, borderwidth=0,
                                    activebackground="white",
                                    command=lambda: controller.show_frame(Subjects))

        button_norsk.place(x=120, y=120)
        button_naturfag.place(x=470, y=180)

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: return_to_menu())
        button_return.place(x=10, y=10)

        menu_sound = pygame.mixer.Sound("Ressurser/Lyd/menu.wav")

        def return_to_menu():
            global BeenBackToMenu
            if not BeenBackToMenu:
                pygame.mixer.stop()
                pygame.mixer.Sound.play(menu_sound)
                BeenBackToMenu = True
            controller.show_frame(Menu)


class Games(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        label_tittel = tk.Label(self, text="GAMES", font=LARGE_FONT)
        label_tittel.configure(background="white")
        label_tittel.pack(pady=10, padx=5)

        label_dev = tk.Label(self, text="(Under development)", font=MEDIUM_FONT)
        label_dev.configure(background="white")
        label_dev.place(x=445, y=377)

        label_mem_game = tk.Label(self, text="Memory Game", font=LARGE_FONT)
        label_mem_game.configure(background="white")
        label_mem_game.place(x=142, y=370)

        photo_memory = tk.PhotoImage(file="Ressurser/GUI elementer/memorygame.png")
        img_memory = tk.Label(self, anchor="w", image=photo_memory)
        img_memory.image = photo_memory
        button_memory = tk.Button(self, command=lambda: go_memory())
        button_memory.config(image=photo_memory, background="white", highlightthickness=0, borderwidth=0,
                             activebackground="white")
        button_memory.place(x=150, y=150, width=200, height=200)

        photo_what = tk.PhotoImage(file="Ressurser/GUI elementer/wut.png")
        img_what = tk.Label(self, anchor="w", image=photo_what)
        img_what.image = photo_what
        button_what = tk.Button(self, command=lambda: controller.show_frame(Games))
        button_what.config(image=photo_what, background="white", highlightthickness=0, borderwidth=0,
                           activebackground="white")
        button_what.place(x=450, y=150, width=200, height=200)

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: return_to_menu())
        button_return.place(x=10, y=10)

        menu_sound = pygame.mixer.Sound("Ressurser/Lyd/menu.wav")
        memory_sound = pygame.mixer.Sound("Ressurser/Lyd/playingwith.wav")

        def return_to_menu():
            global BeenBackToMenu
            if not BeenBackToMenu:
                pygame.mixer.stop()
                pygame.mixer.Sound.play(menu_sound)
                BeenBackToMenu = True
            controller.show_frame(Menu)

        def go_memory():
            global BeenToMemoryMenu
            if not BeenToMemoryMenu:
                pygame.mixer.stop()
                pygame.mixer.Sound.play(memory_sound)
                BeenToMemoryMenu = True
            controller.show_frame(MemoryMenu)


class MemoryMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        memorystart_sound = pygame.mixer.Sound("Ressurser/Lyd/memorystart.wav")

        label_tittel = tk.Label(self, text="MEMORY GAME", font=LARGE_FONT)
        label_tittel.configure(background="white")
        label_tittel.pack(pady=10, padx=5)

        photo_memory = tk.PhotoImage(file="Ressurser/GUI elementer/singleplayer.png")
        img_memory = tk.Label(self, anchor="w", image=photo_memory)
        img_memory.image = photo_memory
        button_memory = tk.Button(self, command=lambda: singleplayer())
        button_memory.config(image=photo_memory, background="white", highlightthickness=0, borderwidth=0,
                             activebackground="white")
        button_memory.place(x=150, y=150, width=200, height=200)

        photo_what = tk.PhotoImage(file="Ressurser/GUI elementer/multiplayer.png")
        img_what = tk.Label(self, anchor="w", image=photo_what)
        img_what.image = photo_what
        button_what = tk.Button(self, command=lambda: multiplayer())
        button_what.config(image=photo_what, background="white", highlightthickness=0, borderwidth=0,
                           activebackground="white")
        button_what.place(x=450, y=150, width=200, height=200)

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: controller.show_frame(Games))
        button_return.place(x=10, y=10)

        label1_p = tk.Label(self, text="Single Player", font=LARGE_FONT)
        label1_p.configure(background="white")
        label1_p.place(x=145, y=370)

        label2_p = tk.Label(self, text="Two Players", font=LARGE_FONT)
        label2_p.configure(background="white")
        label2_p.place(x=460, y=370)

        def singleplayer():
            controller.show_frame(MemoryP1)
            pygame.mixer.stop()
            pygame.mixer.Sound.play(memorystart_sound)

        def multiplayer():
            controller.show_frame(MemoryP2)
            pygame.mixer.stop()
            pygame.mixer.Sound.play(memorystart_sound)


class MemoryP1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, activebackground="white",
                                  borderwidth=0, command=lambda: controller.show_frame(MemoryMenu))

        from Memory1P import MemGame
        x = MemGame(self)
        x.place(x=120, y=20)
        button_return.place(x=10, y=10)


class MemoryP2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, activebackground="white",
                                  borderwidth=0, command=lambda: controller.show_frame(Games))

        from Memory2P import MemGame
        x = MemGame(self)
        x.place(x=120, y=20)
        button_return.place(x=10, y=10)


class Translate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="white")

        label_tittel = tk.Label(self, text="TRANSLATE", font=LARGE_FONT)
        label_tittel.pack(pady=10, padx=10)
        label_tittel.configure(background="white")

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: return_to_menu())
        button_return.place(x=10, y=10)

        hei_sound = pygame.mixer.Sound("Ressurser/Lyd/hei.wav")
        heter_sound = pygame.mixer.Sound("Ressurser/Lyd/heter.wav")
        spille_sound = pygame.mixer.Sound("Ressurser/Lyd/spille.wav")

        photo_hello = tk.PhotoImage(file="Ressurser/GUI elementer/hello.png")
        img_knapp = tk.Label(self, anchor="s", image=photo_hello)
        img_knapp.image = photo_hello
        img_knapp.config(background="white")

        photo_name = tk.PhotoImage(file="Ressurser/GUI elementer/name.png")
        img_name = tk.Label(self, anchor="s", image=photo_name)
        img_name.image = photo_name
        img_name.config(background="white")

        photo_game = tk.PhotoImage(file="Ressurser/GUI elementer/game.png")
        img_game = tk.Label(self, anchor="s", image=photo_game)
        img_game.image = photo_game
        img_game.config(background="white")

        button_b = tk.Button(self, image=photo_hello, highlightthickness=0, borderwidth=0, activebackground="white",
                             text="Hei, jeg heter buddy!",
                             command=lambda: hei())
        button_a = tk.Button(self, image=photo_name, highlightthickness=0, borderwidth=0, activebackground="white",
                             text="Hva heter du?",
                             command=lambda: heter())
        button_c = tk.Button(self, image=photo_game, highlightthickness=0, borderwidth=0, activebackground="white",
                             text="Vil du spille et spill?",
                             command=lambda: spille())

        button_a.configure(background='white', font=MEDIUM_FONT, fg='white')  # height=2, width=20,
        button_b.configure(background='white', font=MEDIUM_FONT, fg='white')
        button_c.configure(background='white', font=MEDIUM_FONT, fg='white')

        button_b.place(x=210, y=140)
        button_a.place(x=210, y=240)
        button_c.place(x=210, y=340)

        menu_sound = pygame.mixer.Sound("Ressurser/Lyd/menu.wav")

        def return_to_menu():
            global BeenBackToMenu
            if not BeenBackToMenu:
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
        repeat_sound = pygame.mixer.Sound("Ressurser/Lyd/repeat.wav")
        hei_sound = pygame.mixer.Sound("Ressurser/Lyd/heijegheter.wav")

        photo_return = tk.PhotoImage(file="Ressurser/GUI elementer/returnknapp.png")
        img_return = tk.Label(self, anchor="s", image=photo_return)
        img_return.image = photo_return
        button_return = tk.Button(self, image=photo_return, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  command=lambda: controller.show_frame(Subjects))
        button_return.place(x=10, y=10)

        label_tittel = tk.Label(self, text="NORWEGIAN", font=LARGE_FONT)
        label_tittel.pack(pady=10, padx=10)
        label_tittel.configure(background="white")

        label_hi = tk.Label(self, text="       English: Hi, my name is... \nNorwegian: Hei, jeg heter...",
                            font=MEDIUM_FONT)
        label_hi.place(x=220, y=100)
        label_hi.config(bg="white")

        photo_buddy = tk.PhotoImage(file="Ressurser/GUI elementer/buddytalkingsmall.png")
        img_buddy = tk.Label(self, anchor="s", image=photo_buddy, highlightthickness=0, borderwidth=0, bg="white")
        img_buddy.image = photo_buddy
        img_buddy.place(x=330, y=200)

        photo_orange_man = tk.PhotoImage(file="Ressurser/GUI elementer/orangetalking.png")
        img_orange_man = tk.Label(self, anchor="s", image=photo_orange_man, highlightthickness=0, borderwidth=0,
                                  bg="white")
        img_orange_man.image = photo_orange_man
        img_orange_man.place(x=-200, y=200)

        photo_knapp = tk.PhotoImage(file="Ressurser/GUI elementer/repeat.png")
        img_knapp = tk.Label(self, anchor="s", image=photo_knapp)
        img_knapp.image = photo_knapp
        img_knapp.config(background="white")

        button_repeat = tk.Button(self, image=photo_knapp, highlightthickness=0, borderwidth=0,
                                  activebackground="white",
                                  text="Hei, jeg heter buddy!", bg="white", command=lambda: repeat_after_me())
        button_repeat.place(x=200, y=390)

        def repeat_after_me():
            repeat()
            self.after(2000, hei)
            self.after(4000, show_orange_man)
            self.after(6000, correct)

        def correct():
            pygame.mixer.Sound.play(correct_sound)

        def show_orange_man():
            img_buddy.place(x=-200, y=200)
            img_orange_man.place(x=330, y=200)

        def hei():
            pygame.mixer.Sound.play(hei_sound)

        def repeat():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(repeat_sound)


app = BuddyOS()
app.mainloop()
