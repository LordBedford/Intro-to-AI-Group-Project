from tkinter import *
import random
import numpy as np
import MapCreator
import os


class MapMaker:

    def __init__(self):
        self.window = Tk()
        # self.window.protocol("WM_DELETE_WINDOW", on_closing)
        self.labels = []
        self.c = Canvas(self.window, width=1500, height=900)
        self.c.pack()
        self.colors = ["black", "green", "orange", "blue", "white", "yellow", "red"]
        self.button = Button(self.window, text='New Map', width=25, command=self.newMap)
        self.button2 = Button(self.window, text='Save', width=25, command=self.save)
        self.button3 = Button(self.window, text='Load', width=25, command=self.load)
        self.button.place(x=0, y=0)
        self.button2.place(x=200, y=0)
        self.button3.place(x=400, y=0)
        self.savefile = open("maps.txt", 'ab')
        self.saves = 0

    def updatewindow(self):
        print("UPDATING")
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(i, " ", j)
                (self.c.create_rectangle(5 * (i + 2), 5 * (j + 8), 5 * (i + 3), 5 * (j + 9),
                                         fill=self.colors[int(self.map[i][j])],
                                         outline='black'))
                self.c.pack()

    def tick(self):
        self.window.update()

    def save(self):
       # for i in range(len(self.map)):
        #    np.savetxt(self.savefile, self.map[i], fmt='%s',newline=' ')
        temp = np.array(self.map)
        np.savetxt(self.savefile, temp, fmt='%s')
        print("Saved!")
        self.saves = self.saves + 1

    def load(self):
        tempCol = []
        tempFile = open("maps.txt", 'r')
        i = 1
        for lines in tempFile.readlines():
           # if i > ((120 * (self.saves - 1)) and i <= (120 * self.saves)):
            lines = lines.strip()
            tempRow = []
            for num in lines:
                if not (num == ' '):
                      tempRow.append(num)
            tempCol.append(tempRow)

            i += 1

        self.map = tempCol
        # for i in range(len(self.map)):
        #   for j in range(len(self.map[i])):
        #      print(self.map[i][j])
        self.updatewindow()

    def newMap(self):
        print("NEW MAP!")
        self.map = MapCreator.mapGen(120, 160)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                (self.c.create_rectangle(5 * (i + 2), 5 * (j + 8), 5 * (i + 3), 5 * (j + 9),
                                         fill=self.colors[int(self.map[i][j])],
                                         outline='black'))
