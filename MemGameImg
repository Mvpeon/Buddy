import tkinter as tk
from random import randint
from random import shuffle
import pygame
pygame.init()

class Controller(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        if True:
            self.frames = {}
            for F in (PageMG,):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("PageMG")
        self.geometry("800x480")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PageMG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        x = MemGame(self)
        x.pack()


class Tile(object):
    def __init__(self, canvas, x, y, image, cardback):
        self.cardback = cardback
        self.canvas = canvas
        self.y = y
        self.x = x
        self.image = image

    # flips tile down
    def drawFaceDown(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill = "white")
        self.canvas.create_image(self.x + 50, self.y + 50, image=self.cardback)
        self.isFaceUp = False

    # flips tile up
    def drawFaceUp(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill = "white")
        self.canvas.create_image(self.x + 50, self.y + 50, image=self.image)
        self.isFaceUp = True

    def isUnderMouse(self, event):
        if(event.x > self.x and event.x < self.x + 100):
            if(event.y > self.y and event.y < self.y + 100):
                return True


class MemGame(tk.Frame):
    def __init__(self, master):
        super(MemGame, self).__init__(master)

        # restart button
        photoRestart = tk.PhotoImage(file="restart.png")
        imgRestart = tk.Label(self, anchor="s", image=photoRestart)
        imgRestart.image = photoRestart
        buttonRestart = tk.Button(self, activebackground="white",
                                  image=photoRestart, highlightthickness=0, borderwidth=0,
                                  command=lambda: self.restart())
        buttonRestart.place(x=560, y=200)

        # animals
        photoDog = tk.PhotoImage(file="Dyr/dog.png")
        photoElefant = tk.PhotoImage(file="Dyr/elefant.png")
        photoFlamingo = tk.PhotoImage(file="Dyr/flamingo.png")
        photoFlodhest = tk.PhotoImage(file="Dyr/flodhest.png")
        photoKamel = tk.PhotoImage(file="Dyr/kamel.png")
        photoKatt = tk.PhotoImage(file="Dyr/katt.png")
        photoKrokodille = tk.PhotoImage(file="Dyr/krokodille.png")
        photoNeshorn = tk.PhotoImage(file="Dyr/neshorn.png")
        photoSkilpadde = tk.PhotoImage(file="Dyr/skilpadde.png")
        photoStruts = tk.PhotoImage(file="Dyr/struts.png")
        photoZebra = tk.PhotoImage(file="Dyr/zebra.png")
        photoLove = tk.PhotoImage(file="Dyr/love.png")

        # cardback
        photoCardback = tk.PhotoImage(file="cardback.png")
        self.cardback = photoCardback

        # sound effects
        self.riktig_sound = pygame.mixer.Sound("riktig.wav")
        self.click_sound = pygame.mixer.Sound("camerashutter.wav")
        self.gratulerer_sound = pygame.mixer.Sound("cheer.wav")

        self.configure(width=650, height=480, bg="white")
        self.canvas = tk.Canvas(self, bg="white", width=550, height=480, highlightthickness=0, borderwidth=0)
        self.canvas.place(x=0, y=-30)
        self.tiles = []
        self.images = [
            photoDog,
            photoElefant,
            photoFlamingo,
            photoFlodhest,
            photoKamel,
            photoKatt,
            photoKrokodille,
            photoNeshorn,
            photoSkilpadde,
            photoStruts,
            photoZebra,
            photoLove
        ]

        self.texts = {
            "Dog",
            "Elephant",
            "Flamingo",
            "Hippopotamus",
            "Camel",
            "Cat",
            "Crocodile",
            "Rhinoceros",
            "Turtle",
            "Ostrich",
            "Zebra",
            "Lion"
        }

        selected = []
        for i in range(10):
            randomInd = randint(0, len(self.images) - 1)
            animalImg = self.images[randomInd]
            selected.append(animalImg)
            selected.append(animalImg)
            del self.images[randomInd]
        shuffle(selected)
        self.flippedTiles = []
        NUM_COLS = 5
        NUM_ROWS = 4

        self.score = 0

        for x in range(0, NUM_COLS):
            for y in range(0, NUM_ROWS):
                self.tiles.append(Tile(self.canvas, x * 108 + 10, y * 108 + 40, selected.pop(), photoCardback))

        for i in range(len(self.tiles)):
            self.tiles[i].drawFaceDown()
        self.flippedThisTurn = 0
        self.canvas.bind("<Button-1>", self.mouseClicked)

    # event for clicking on a tile
    def mouseClicked(self, event):
        for tile in self.tiles:
            if tile.isUnderMouse(event) and (self.flippedThisTurn < 2):
                if (not(tile.isFaceUp)):
                    self.clickSound()
                    tile.drawFaceUp()
                    self.flippedTiles.append(tile)
                    self.flippedThisTurn += 1

                # when two new tiles are flipped, checks if they match
                if (self.flippedThisTurn == 2):
                    if (self.flippedTiles[-1].image == self.flippedTiles[-2].image):
                        self.riktig()
                        self.score += 1
                    self.after(1000, self.checkTiles)

    # checks the last two flipped tiles and flips them back down if they don't match
    def checkTiles(self):
        self.flippedThisTurn = 0
        if not(self.flippedTiles[-1].image == self.flippedTiles[-2].image): #check last two elements
            self.flippedTiles[-1].drawFaceDown()
            self.flippedTiles[-2].drawFaceDown()
            del self.flippedTiles[-2:]

        # plays sound effect when completing the game
        if (self.score == 10):
            self.after(100, self.gratulerer)

    # flips all the tiles face down
    def restart(self):
        for i in range(len(self.tiles)):
            self.tiles[i].drawFaceDown()
            self.score = 0
            self.clickSound()

    # sound effect for finding two matching tiles
    def riktig(self):
        pygame.mixer.Sound.play(self.riktig_sound)
        pygame.mixer.music.stop()

    # sound effect for completing the game
    def gratulerer(self):
        pygame.mixer.Sound.play(self.gratulerer_sound)
        pygame.mixer.music.stop()

    # button click sound effect
    def clickSound(self):
        pygame.mixer.Sound.play(self.click_sound)
        pygame.mixer.music.stop()

if __name__ == '__main__':
    c = Controller()
    c.mainloop()
