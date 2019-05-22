import tkinter as tk
from random import randint
from random import shuffle
#import time

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
        self.geometry("500x400")

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
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas
        self.y = y
        self.x = x
        self.text = text

    def drawFaceDown(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill = "blue")
        self.isFaceUp = False

    def drawFaceUp(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill = "blue")
        self.canvas.create_text(self.x + 35, self.y + 35, text = self.text, width = 70, fill = "white", font='Helvetica 12 bold')
        self.isFaceUp = True

    def isUnderMouse(self, event):
        if(event.x > self.x and event.x < self.x + 70):
            if(event.y > self.y and event.y < self.y + 70):
                return True


class MemGame(tk.Frame):
    def __init__(self, master):
        super(MemGame, self).__init__(master)
        self.configure(width=500, height=500)
        self.canvas = tk.Canvas(self, width=400, height=350, bg="white")
        self.canvas.place(x=50, y=150)
        self.tiles = []
        self.colors = [
            "Eple",
            "Appelsin",
            "Banan",
            "Agurk",
            "Brokkoli",
            "Tomat",
            "Sitron",
            "Melon",
            "Hvitløk",
            "Erter",
            "Jordbær",
            "Blåbær"
        ]

        selected = []
        for i in range(10):
            randomInd = randint(0, len(self.colors) - 1)
            color = self.colors[randomInd]
            selected.append(color)
            selected.append(color)
            del self.colors[randomInd]
        shuffle(selected)
        self.flippedTiles = []
        NUM_COLS = 5
        NUM_ROWS = 4

        for x in range(0, NUM_COLS):
            for y in range(0, NUM_ROWS):
                self.tiles.append(Tile(self.canvas, x * 78 + 10, y * 78 + 40, selected.pop()))

        for i in range(len(self.tiles)):
            self.tiles[i].drawFaceDown()
        self.flippedThisTurn = 0
        self.bind("<Button-1>", self.mouseClicked)

    # def mouseClicked(self):
    #     for i in range(len(self.tiles)):
    #         if self.tiles[i].isUnderMouse(self):
    #             if (len(self.flippedTiles) < 2 and not(self.tiles[i].isFaceUp)) :
    #                 self.tiles[i].drawFaceUp()
    #                 self.flippedTiles.append(self.tiles[i])
    #             if (len(self.flippedTiles) == 2):
    #                 if not(self.flippedTiles[0].text == self.flippedTiles[1].text):
    #                     time.sleep(1)
    #                     self.flippedTiles[0].drawFaceDown()
    #                     self.flippedTiles[1].drawFaceDown()

    def mouseClicked(self, event):
        for tile in self.tiles:
            if tile.isUnderMouse(event):
                if (not(tile.isFaceUp)) :
                    tile.drawFaceUp()
                    self.flippedTiles.append(tile)
                    self.flippedThisTurn += 1

                if (self.flippedThisTurn == 2):
                    self.after(1000, self.checkTiles)
                    self.flippedThisTurn = 0

    def checkTiles(self):
        if not(self.flippedTiles[-1].text == self.flippedTiles[-2].text): #check last two elements
            self.flippedTiles[-1].drawFaceDown()
            self.flippedTiles[-2].drawFaceDown()
            del self.flippedTiles[-2:]


if __name__ == '__main__':
    c = Controller()
    c.mainloop()
