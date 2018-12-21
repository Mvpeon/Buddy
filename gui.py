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


        label = tk.Label(self, text="Meny", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(PageOne))

        button2 = tk.Button(self, text="Kommuniser",
                            command=lambda: controller.show_frame(PageTwo))

        button3 = tk.Button(self, text="Lær deg",
                            command=lambda: controller.show_frame(StartPage))

        button4 = tk.Button(self, text="Spill",
                            command=lambda: controller.show_frame(PageOne))

        button1.configure(background='orange', height = 2, width = 20, fg='white')
        button2.configure(background='purple', height = 2, width = 20, fg='white')
        button3.configure(background='purple', height = 2, width = 20, fg='white')
        button4.configure(background='purple', height = 2, width = 20, fg='white')

        #button1.pack(padx=5, pady=5)
        button2.pack(padx=5, pady=5)
        button3.pack(padx=5, pady=5)
        button4.pack(padx=5, pady=5)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Spill", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        photo = tk.PhotoImage(file="mario.png")
        photo2 = tk.PhotoImage(file="luigi.png")
        photo3 = tk.PhotoImage(file="toad.png")
        labelimg = tk.Label(self, anchor="s", image=photo)
        labelimg.image = photo  # keep a reference!
        buttonimg = tk.Label(self, anchor="w", image=photo2)
        buttonimg.image = photo2
        buttonimg2 = tk.Label(self, anchor="w", image=photo3)
        buttonimg2.image = photo3

        button = tk.Button(self,
                           command=lambda: controller.show_frame(StartPage))

        button2 = tk.Button(self,
                            command=lambda: controller.show_frame(PageTwo))
        button.configure(background='orange', height=2, width=20, fg='white', text="Meny")
        button2.configure(background='purple', padx=20, pady=5, fg='white', text="Visit Page 2")
        button.pack(padx=5, pady=5)
        #button2.pack(padx=5, pady=5)

        luigi = tk.Button(self,
                          command=lambda: controller.show_frame(PageCommunicate))
        luigi.config(image=photo2)
        luigi.place(x=100, y=160, width=128, height=128)

        toad = tk.Button(self,
                         command=lambda: controller.show_frame(PageOne))
        toad.config(image=photo3)
        toad.place(x=600, y=160, width=128, height=128)

        labelimg.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kommuniser", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.configure(background='orange', height=2, width=20, fg='white')
        button1.pack()


class PageCommunicate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Kommuniser",
                            command=lambda: controller.show_frame(StartPage))
        button1.configure(background='orange', height=2, width=20, fg='white')
        button1.pack()

        button2 = tk.Button(self, text="Lær deg",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

        button3 = tk.Button(self, text="Spill",
                            command=lambda: controller.show_frame(StartPage))
        button3.pack()


app = SeaofBTCapp()
app.mainloop()