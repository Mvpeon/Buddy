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
        buttonRestart.place(x=560, y=197)

        self.score = 0

        # plain image PNGs
        photoDog = tk.PhotoImage(file="Dyr/dog.png")
        photoElephant = tk.PhotoImage(file="Dyr/elephant.png")
        photoFlamingo = tk.PhotoImage(file="Dyr/flamingo.png")
        photoHippo = tk.PhotoImage(file="Dyr/hippo.png")
        photoCamel = tk.PhotoImage(file="Dyr/camel.png")
        photoCat = tk.PhotoImage(file="Dyr/cat.png")
        photoCrocodile = tk.PhotoImage(file="Dyr/crocodile.png")
        photoRhinoceros = tk.PhotoImage(file="Dyr/rhinoceros.png")
        photoTurtle = tk.PhotoImage(file="Dyr/turtle.png")
        photoOstrich = tk.PhotoImage(file="Dyr/ostrich.png")
        photoZebra = tk.PhotoImage(file="Dyr/zebra.png")
        photoLion = tk.PhotoImage(file="Dyr/lion.png")

        # plain text PNGs
        photoDogText = tk.PhotoImage(file="Dyr/dogtext.png")
        photoElephantText = tk.PhotoImage(file="Dyr/elephanttext.png")
        photoFlamingoText = tk.PhotoImage(file="Dyr/flamingotext.png")
        photoHippoText = tk.PhotoImage(file="Dyr/hippotext.png")
        photoCamelText = tk.PhotoImage(file="Dyr/cameltext.png")
        photoCatText = tk.PhotoImage(file="Dyr/cattext.png")
        #photoCrocodileText = tk.PhotoImage(file="Dyr/crocodiletext.png")
        #photoRhinocerosText = tk.PhotoImage(file="Dyr/rhinocerostext.png")
        #photoTurtleText = tk.PhotoImage(file="Dyr/turtletext.png")
        #photoOstrichText = tk.PhotoImage(file="Dyr/ostrichtext.png")
        #photoZebraText = tk.PhotoImage(file="Dyr/zebratext.png")
        #photoLionText = tk.PhotoImage(file="Dyr/liontext.png")

        # norwegian text tiles
        #photoNorDog = tk.PhotoImage(file="Dyr/N-dog.png")
        #photoNorElephant = tk.PhotoImage(file="Dyr/N-elephant.png")
        #photoNorFlamingo = tk.PhotoImage(file="Dyr/N-flamingo.png")
        #photoNorHippo = tk.PhotoImage(file="Dyr/N-hippo.png")
        #photoNorCamel = tk.PhotoImage(file="Dyr/N-camel.png")
        #photoNorCat = tk.PhotoImage(file="Dyr/N-cat.png")
        photoNorCrocodile = tk.PhotoImage(file="Dyr/N-crocodile.png")
        photoNorRhinoceros = tk.PhotoImage(file="Dyr/N-rhinoceros.png")
        photoNorTurtle = tk.PhotoImage(file="Dyr/N-turtle.png")
        photoNorOstrich = tk.PhotoImage(file="Dyr/N-ostrich.png")
        photoNorZebra = tk.PhotoImage(file="Dyr/N-zebra.png")
        photoNorLion = tk.PhotoImage(file="Dyr/N-lion.png")

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

        # plain text PNGs
        self.textImages = [
            photoDogText,
            photoElephantText,
            photoFlamingoText,
            photoHippoText,
            photoCamelText,
            photoCatText,
            photoNorCrocodile,
            photoNorRhinoceros,
            photoNorTurtle,
            photoNorOstrich,
            photoNorZebra,
            photoNorLion
        ]

        self.dict = {
            "photoDogTag": photoDog,
        }

        # creating a dictionary that will be used for matching different plain images with text images of same animals
        self.all_tiles = self.images + self.textImages
        self.matches = {
            k: v for (k, v) in zip(self.images, self.textImages)
        }
        self.matches.update([(k, v) for (k, v) in zip(self.textImages, self.images)])

        selected = []
        for i in range(10):
            randomInd = randint(0, len(self.images) - 1)
            animalImg = self.images[randomInd]
            animalImgText = self.textImages[randomInd]
            selected.append(animalImg)
            selected.append(animalImgText)
            del self.images[randomInd]
            del self.textImages[randomInd]
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

                # when two new tiles are flipped, plays sound effect and increases score if they match
                if (self.flippedThisTurn == 2):
                    var1 = self.flippedTiles[-1].image
                    var2 = self.flippedTiles[-2].image
                    if (self.matches.get(var1) == var1 or self.matches.get(var1) == var2 or self.matches.get(var2) == var2): #check last two elements
                        self.riktig()
                        self.score += 1
                    self.after(1000, self.checkTiles) # then performs another check after a short delay

    # checks the last two flipped tiles and resets them if they don't match
    def checkTiles(self):
        self.flippedThisTurn = 0
        var1 = self.flippedTiles[-1].image
        var2 = self.flippedTiles[-2].image
        if not (self.matches.get(var1) == var1 or self.matches.get(var1) == var2 or self.matches.get(var2) == var2):
            self.flippedTiles[-1].drawFaceDown()
            self.flippedTiles[-2].drawFaceDown()
            del self.flippedTiles[-2:]

        # plays sound effect when completing the game after a very short delay
        if (self.score == 10):
            self.after(100, self.gratulerer)

    # flips all the tiles face down and resets score
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