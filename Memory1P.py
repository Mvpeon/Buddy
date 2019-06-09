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


class Tile(object): # this class is used for creating the tiles
    def __init__(self, canvas, x, y, image, cardback):
        self.cardback = cardback
        self.canvas = canvas
        self.y = y
        self.x = x
        self.image = image

    # flips tile down
    def drawFaceDown(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill = "#fadebe")
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
        photoRestart = tk.PhotoImage(file="Ressurser/GUI elementer/restart.png")
        imgRestart = tk.Label(self, anchor="s", image=photoRestart)
        imgRestart.image = photoRestart
        buttonRestart = tk.Button(self, activebackground="white",
                                  image=photoRestart, highlightthickness=0, borderwidth=0,
                                  command=lambda: self.restart())
        buttonRestart.place(x=560, y=197)

        self.photoArrow = tk.PhotoImage(file="Ressurser/GUI elementer/arrow.png")
        self.imgArrow = tk.Label(self, anchor="s", image=self.photoArrow, bg="white")
        self.imgArrow.image = self.photoArrow
        self.imgArrow.place(x=0, y=0) #x=560, y=250

        self.configure(width=650, height=480, bg="white")
        self.canvas = tk.Canvas(self, bg="white", width=550, height=480, highlightthickness=0, borderwidth=0)
        self.canvas.place(x=0, y=-30)
        self.tiles = []
        self.score = 0

        # plain image PNGs
        photoDog = tk.PhotoImage(file="Ressurser/Dyr/dog.png")
        photoElephant = tk.PhotoImage(file="Ressurser/Dyr/elephant.png")
        photoFlamingo = tk.PhotoImage(file="Ressurser/Dyr/flamingo.png")
        photoHippo = tk.PhotoImage(file="Ressurser/Dyr/hippo.png")
        photoCamel = tk.PhotoImage(file="Ressurser/Dyr/camel.png")
        photoCat = tk.PhotoImage(file="Ressurser/Dyr/cat.png")
        photoCrocodile = tk.PhotoImage(file="Ressurser/Dyr/crocodile.png")
        photoRhinoceros = tk.PhotoImage(file="Ressurser/Dyr/rhinoceros.png")
        photoTurtle = tk.PhotoImage(file="Ressurser/Dyr/turtle.png")
        photoOstrich = tk.PhotoImage(file="Ressurser/Dyr/ostrich.png")
        photoZebra = tk.PhotoImage(file="Ressurser/Dyr/zebra.png")
        photoLion = tk.PhotoImage(file="Ressurser/Dyr/lion.png")

        # norwegian text tiles
        photoNorDog = tk.PhotoImage(file="Ressurser/Dyr/N-dog.png")
        photoNorElephant = tk.PhotoImage(file="Ressurser/Dyr/N-elephant.png")
        photoNorFlamingo = tk.PhotoImage(file="Ressurser/Dyr/N-flamingo.png")
        photoNorHippo = tk.PhotoImage(file="Ressurser/Dyr/N-hippo.png")
        photoNorCamel = tk.PhotoImage(file="Ressurser/Dyr/N-camel.png")
        photoNorCat = tk.PhotoImage(file="Ressurser/Dyr/N-cat.png")
        photoNorCrocodile = tk.PhotoImage(file="Ressurser/Dyr/N-crocodile.png")
        photoNorRhinoceros = tk.PhotoImage(file="Ressurser/Dyr/N-rhinoceros.png")
        photoNorTurtle = tk.PhotoImage(file="Ressurser/Dyr/N-turtle.png")
        photoNorOstrich = tk.PhotoImage(file="Ressurser/Dyr/N-ostrich.png")
        photoNorZebra = tk.PhotoImage(file="Ressurser/Dyr/N-zebra.png")
        photoNorLion = tk.PhotoImage(file="Ressurser/Dyr/N-lion.png")

        # cardback
        photoCardback = tk.PhotoImage(file="Ressurser/GUI elementer/cardback1P.png")
        self.cardback = photoCardback

        # sound effects
        self.correct_sound = pygame.mixer.Sound("Ressurser/Lyd/correct.wav")
        self.click_sound = pygame.mixer.Sound("Ressurser/Lyd/camerashutter.wav")
        self.gratulerer_sound = pygame.mixer.Sound("Ressurser/Lyd/cheer.wav")

        # plain image PNGs
        self.images = [
            photoDog,
            photoElephant,
            photoFlamingo,
            photoHippo,
            photoCamel,
            photoCat,
            photoCrocodile,
            photoRhinoceros,
            photoTurtle,
            photoOstrich,
            photoZebra,
            photoLion
        ]

        # norwegian text tiles
        self.norImages = [
            photoNorDog,
            photoNorElephant,
            photoNorFlamingo,
            photoNorHippo,
            photoNorCamel,
            photoNorCat,
            photoNorCrocodile,
            photoNorRhinoceros,
            photoNorTurtle,
            photoNorOstrich,
            photoNorZebra,
            photoNorLion
        ]

        # creating a dictionary that will be used for matching different plain images with text images of same animals
        self.all_tiles = self.images + self.norImages
        self.matches = {
            k: v for (k, v) in zip(self.images, self.norImages)
        }
        self.matches.update([(k, v) for (k, v) in zip(self.norImages, self.images)])

        selected = []
        for i in range(10):
            randomInd = randint(0, len(self.images) - 1)
            animalImg = self.images[randomInd]
            animalImgText = self.norImages[randomInd]
            selected.append(animalImg)
            selected.append(animalImgText)
            del self.images[randomInd]
            del self.norImages[randomInd]
        shuffle(selected)
        self.flippedTiles = []
        NUM_COLS = 5
        NUM_ROWS = 4

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

                # performs a check when two new tiles are flipped
                if (self.flippedThisTurn == 2):
                    self.checkTiles()

    # method for checking tiles
    def checkTiles(self):
        var1 = self.flippedTiles[-1].image
        var2 = self.flippedTiles[-2].image
        if (self.matches.get(var1) == var1 or self.matches.get(var1) == var2 or self.matches.get(var2) == var2):
            self.correct()
            self.score += 1
            del self.flippedTiles[-2:]
        else:
            self.after(1000, self.flippedTiles[-1].drawFaceDown)
            self.after(1000, self.flippedTiles[-2].drawFaceDown)
        self.flippedThisTurn = 0

        # plays sound effect when completing the game after a short delay
        if (self.score == 10):
            self.imgArrow.place(x=560, y=250)
            self.after(700, self.gratulerer)

    # resets the game
    def restart(self):
        for i in range(len(self.tiles)):
            self.tiles[i].drawFaceDown()
        self.score = 0
        self.clickSound()
        self.imgArrow.place(x=0, y=0)
        self.flippedTiles = []
        self.flippedThisTurn = 0

    # sound effect for finding two matching tiles
    def correct(self):
        pygame.mixer.Sound.play(self.correct_sound)

    # sound effect for completing the game
    def gratulerer(self):
        pygame.mixer.Sound.play(self.gratulerer_sound)

    # button click sound effect
    def clickSound(self):
        pygame.mixer.Sound.play(self.click_sound)

if __name__ == '__main__':
    c = Controller()
    c.mainloop()