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
