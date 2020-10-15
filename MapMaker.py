from tkinter import *

import Astar


class MapMaker:



    def __init__(self):
        self.window = Tk()
        #self.window.protocol("WM_DELETE_WINDOW", on_closing)
        self.map = Astar.mapGen()
        self.labels = []
        self.c = Canvas(self.window, width=250, height=200)
        self.c.pack()


    def updatewindow(self):
        self.window.update()
        for i in range(len(self.map)):
            boxes = []
            for j in range(len(self.map[i])):
                boxes.append(self.c.create_rectangle(20 * i, 20 * j, 20 * (i + 1), 20 * (j + 1), fill="blue",
                                                          outline='blue'))
                self.c.pack()
            self.labels.append(boxes)



