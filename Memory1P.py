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
        # how a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class PageMG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        x = MemGame(self)
        x.pack()


class Tile(object):  # this class is used for creating the tiles
    def __init__(self, canvas, x, y, image, cardback):
        self.cardback = cardback
        self.canvas = canvas
        self.y = y
        self.x = x
        self.image = image

    # flips tile down
    def draw_face_down(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill="#fadebe")
        self.canvas.create_image(self.x + 50, self.y + 50, image=self.cardback)
        self.is_face_up = False

    # flips tile up
    def draw_face_up(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill="white")
        self.canvas.create_image(self.x + 50, self.y + 50, image=self.image)
        self.is_face_up = True

    def is_under_mouse(self, event):
        if event.x > self.x and event.x < self.x + 100:
            if event.y > self.y and event.y < self.y + 100:
                return True


class MemGame(tk.Frame):
    def __init__(self, master):
        super(MemGame, self).__init__(master)

        # restart button
        photo_restart = tk.PhotoImage(file="Ressurser/GUI elementer/restart.png")
        img_restart = tk.Label(self, anchor="s", image=photo_restart)
        img_restart.image = photo_restart
        button_restart = tk.Button(self, activebackground="white",
                                   image=photo_restart, highlightthickness=0, borderwidth=0,
                                   command=lambda: self.restart())
        button_restart.place(x=560, y=197)

        self.photoArrow = tk.PhotoImage(file="Ressurser/GUI elementer/arrow.png")
        self.imgArrow = tk.Label(self, anchor="s", image=self.photoArrow, bg="white")
        self.imgArrow.image = self.photoArrow
        self.imgArrow.place(x=0, y=0)  # x=560, y=250

        self.configure(width=650, height=480, bg="white")
        self.canvas = tk.Canvas(self, bg="white", width=550, height=480, highlightthickness=0, borderwidth=0)
        self.canvas.place(x=0, y=-30)
        self.tiles = []
        self.score = 0

        # plain image PNGs
        photo_dog = tk.PhotoImage(file="Ressurser/Dyr/dog.png")
        photo_elephant = tk.PhotoImage(file="Ressurser/Dyr/elephant.png")
        photo_flamingo = tk.PhotoImage(file="Ressurser/Dyr/flamingo.png")
        photo_hippo = tk.PhotoImage(file="Ressurser/Dyr/hippo.png")
        photo_camel = tk.PhotoImage(file="Ressurser/Dyr/camel.png")
        photo_cat = tk.PhotoImage(file="Ressurser/Dyr/cat.png")
        photo_crocodile = tk.PhotoImage(file="Ressurser/Dyr/crocodile.png")
        photo_rhinoceros = tk.PhotoImage(file="Ressurser/Dyr/rhinoceros.png")
        photo_turtle = tk.PhotoImage(file="Ressurser/Dyr/turtle.png")
        photo_ostrich = tk.PhotoImage(file="Ressurser/Dyr/ostrich.png")
        photo_zebra = tk.PhotoImage(file="Ressurser/Dyr/zebra.png")
        photo_lion = tk.PhotoImage(file="Ressurser/Dyr/lion.png")

        # norwegian text tiles
        photo_nor_dog = tk.PhotoImage(file="Ressurser/Dyr/N-dog.png")
        photo_nor_elephant = tk.PhotoImage(file="Ressurser/Dyr/N-elephant.png")
        photo_nor_flamingo = tk.PhotoImage(file="Ressurser/Dyr/N-flamingo.png")
        photo_nor_hippo = tk.PhotoImage(file="Ressurser/Dyr/N-hippo.png")
        photo_nor_camel = tk.PhotoImage(file="Ressurser/Dyr/N-camel.png")
        photo_nor_cat = tk.PhotoImage(file="Ressurser/Dyr/N-cat.png")
        photo_nor_crocodile = tk.PhotoImage(file="Ressurser/Dyr/N-crocodile.png")
        photo_nor_rhinoceros = tk.PhotoImage(file="Ressurser/Dyr/N-rhinoceros.png")
        photo_nor_turtle = tk.PhotoImage(file="Ressurser/Dyr/N-turtle.png")
        photo_nor_ostrich = tk.PhotoImage(file="Ressurser/Dyr/N-ostrich.png")
        photo_nor_zebra = tk.PhotoImage(file="Ressurser/Dyr/N-zebra.png")
        photo_nor_lion = tk.PhotoImage(file="Ressurser/Dyr/N-lion.png")

        # cardback
        photo_cardback = tk.PhotoImage(file="Ressurser/GUI elementer/cardback1P.png")
        self.cardback = photo_cardback

        # sound effects
        self.correct_sound = pygame.mixer.Sound("Ressurser/Lyd/correct.wav")
        self.click_sound = pygame.mixer.Sound("Ressurser/Lyd/camerashutter.wav")
        self.gratulerer_sound = pygame.mixer.Sound("Ressurser/Lyd/cheer.wav")
        self.memorystart_sound = pygame.mixer.Sound("Ressurser/Lyd/memorystart.wav")

        # plain image PNGs
        self.images = [
            photo_dog,
            photo_elephant,
            photo_flamingo,
            photo_hippo,
            photo_camel,
            photo_cat,
            photo_crocodile,
            photo_rhinoceros,
            photo_turtle,
            photo_ostrich,
            photo_zebra,
            photo_lion
        ]

        # norwegian text tiles
        self.norImages = [
            photo_nor_dog,
            photo_nor_elephant,
            photo_nor_flamingo,
            photo_nor_hippo,
            photo_nor_camel,
            photo_nor_cat,
            photo_nor_crocodile,
            photo_nor_rhinoceros,
            photo_nor_turtle,
            photo_nor_ostrich,
            photo_nor_zebra,
            photo_nor_lion
        ]

        # creating a dictionary that will be used for matching different plain images with text images of same animals
        self.all_tiles = self.images + self.norImages
        self.matches = {
            k: v for (k, v) in zip(self.images, self.norImages)
        }
        self.matches.update([(k, v) for (k, v) in zip(self.norImages, self.images)])

        selected = []
        for i in range(10):
            random_ind = randint(0, len(self.images) - 1)
            animal_img = self.images[random_ind]
            animal_img_text = self.norImages[random_ind]
            selected.append(animal_img)
            selected.append(animal_img_text)
            del self.images[random_ind]
            del self.norImages[random_ind]
        shuffle(selected)
        self.flippedTiles = []
        num_cols = 5
        num_rows = 4

        for x in range(0, num_cols):
            for y in range(0, num_rows):
                self.tiles.append(Tile(self.canvas, x * 108 + 10, y * 108 + 40, selected.pop(), photo_cardback))

        for i in range(len(self.tiles)):
            self.tiles[i].draw_face_down()
        self.flippedThisTurn = 0
        self.canvas.bind("<Button-1>", self.mouse_clicked)

    # event for clicking on a tile
    def mouse_clicked(self, event):
        for tile in self.tiles:
            if tile.is_under_mouse(event):
                if not tile.is_face_up:
                    self.click_sound()
                    tile.draw_face_up()
                    self.flippedTiles.append(tile)
                    self.flippedThisTurn += 1

                # performs a check when two new tiles are flipped
                if self.flippedThisTurn == 2:
                    self.check_tiles()

    # method for checking tiles
    def check_tiles(self):
        var1 = self.flippedTiles[-1].image
        var2 = self.flippedTiles[-2].image
        if self.matches.get(var1) == var1 or self.matches.get(var1) == var2 or self.matches.get(var2) == var2:
            self.correct()
            self.score += 1
            del self.flippedTiles[-2:]
        else:
            self.after(1000, self.flippedTiles[-1].draw_face_down)
            self.after(1000, self.flippedTiles[-2].draw_face_down)
        self.flippedThisTurn = 0

        # plays sound effect when completing the game after a short delay
        if self.score == 10:
            self.imgArrow.place(x=560, y=250)
            self.after(700, self.gratulerer)

    # resets the game
    def restart(self):
        for i in range(len(self.tiles)):
            self.tiles[i].draw_face_down()
        self.score = 0
        self.click_sound()
        self.imgArrow.place(x=0, y=0)
        self.flippedTiles = []
        self.flippedThisTurn = 0
        pygame.mixer.stop()
        pygame.mixer.Sound.play(self.memorystart_sound)

    # sound effect for finding two matching tiles
    def correct(self):
        pygame.mixer.Sound.play(self.correct_sound)

    # sound effect for completing the game
    def gratulerer(self):
        pygame.mixer.Sound.play(self.gratulerer_sound)

    # button click sound effect
    def click_sound(self):
        pygame.mixer.Sound.play(self.click_sound)


if __name__ == '__main__':
    c = Controller()
    c.mainloop()
