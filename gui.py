import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry("800x480")
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelTittel = tk.Label(self, text="Meny", font=LARGE_FONT)
        buttonKom = tk.Button(self, text="Kommuniser", command=lambda: controller.show_frame(PageTwo))
        buttonLær = tk.Button(self, text="Lær deg", command=lambda: controller.show_frame(StartPage))
        buttonSpill = tk.Button(self, text="Spill", command=lambda: controller.show_frame(PageOne))

        labelTittel.configure(background="white")
        buttonKom.configure(background='purple', height=2, width=20, fg='white')
        buttonLær.configure(background='purple', height=2, width=20, fg='white')
        buttonSpill.configure(background='purple', height=2, width=20, fg='white')

        labelTittel.pack(pady=10, padx=10)
        buttonKom.pack(padx=5, pady=5)
        buttonLær.pack(padx=5, pady=5)
        buttonSpill.pack(padx=5, pady=5)

        self.configure(background="white")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelTittel = tk.Label(self, text="Spill", font=LARGE_FONT)

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
        luigi = tk.Button(self, command=lambda: controller.show_frame(PageOne))
        toad = tk.Button(self, command=lambda: controller.show_frame(PageOne))

        labelTittel.configure(background="white")
        buttonMeny.configure(background='orange', height=2, width=20, fg='white', text="Meny")
        luigi.config(image=photoLuigi)
        toad.config(image=photoToad)
        imgMario.config(background="white")

        labelTittel.pack(pady=10, padx=5)
        buttonMeny.pack(padx=5, pady=5)
        luigi.place(x=100, y=160, width=128, height=128)
        toad.place(x=600, y=160, width=128, height=128)
        imgMario.place(x=300, y=120)

        self.configure(background="white")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelTittel = tk.Label(self, text="Kommuniser", font=LARGE_FONT)
        labelTittel.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Meny", command=lambda: controller.show_frame(StartPage))

        labelTittel.configure(background="white")
        button1.configure(background='orange', height=2, width=20, fg='white')

        button1.pack()

        self.configure(background="white")


app = SeaofBTCapp()
app.mainloop()
