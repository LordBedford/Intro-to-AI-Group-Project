from tkinter import *
import random
import Astar


class MapMaker:

    def __init__(self):
        self.window = Tk()
        # self.window.protocol("WM_DELETE_WINDOW", on_closing)
        self.map = Astar.mapGen()
        self.labels = []
        self.c = Canvas(self.window, width=1000, height=800)
        self.c.pack()
        self.colors = ["blue", "red", "pink", "green"]
        self.button = Button(self.window, text='New Map', width=50, command =self.updatewindow)
        self.button.pack(side="bottom")

    def updatewindow(self):
        print("New MAP!")
        self.map = Astar.mapGen()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):

                (self.c.create_rectangle(5 * (i + 1), 5 * (j + 1), 5 * (i + 2), 5 * (j + 2),
                                                             fill=self.colors[int(self.map[i][j])],
                                                             outline='black'))
                self.c.pack()

    def tick(self):
        self.window.update()


