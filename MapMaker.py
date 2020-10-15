from tkinter import *

import Astar


class MapMaker:



    def __init__(self):
        self.window = Tk()
        #self.window.protocol("WM_DELETE_WINDOW", on_closing)
        self.map = Astar.mapGen()
        self.labels = []
        self.c = Canvas(self.window, width=1500, height=1500)
        self.c.pack()
        colors = ["blue", "red","pink","green"]
        for i in range(len(self.map)):
            boxes = []
            for j in range(len(self.map[i])):
                boxes.append(self.c.create_rectangle(10 * i, 10 * j, 10 * (i + 1), 10 * (j + 1), fill=colors[int(self.map[i][j])],
                                                     outline='black'))
                self.c.pack()
            self.labels.append(boxes)

    def updatewindow(self):
        self.window.update()




