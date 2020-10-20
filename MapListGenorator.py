#Andrew Cater

import MapCreator
import numpy as np
import sys

def mapHelper(x1,y1,x2,y2,array):
    ret = []
    for i in range(len(array)):
        temp = []
        for j in range(len(array[i])):
            if((i == x1) and (j == y1)):
                temp.append("5")
            elif((i == x2) and (j == y2)):
                temp.append("6")
            else:
                temp.append(array[i][j])
        ret.append(temp)
    return ret

for i in range(5):
    map, hard_terrain = MapCreator.mapGen(120, 160)
    for j in range(10):
        posx1, posy1, posx2, posy2 = MapCreator.getCoordinates(map)
        mapTemp = mapHelper(posx1, posy1, posx2, posy2,map)
        savefile = open("maps/map%s/map%s.txt" %(i, j), 'w')
        ogOutPut = sys.stdout
        sys.stdout = savefile
        print(posx1, posy1)
        print(posx2, posy2)
        for x in range(len(hard_terrain)):
            print(hard_terrain[x][0], hard_terrain[x][1])
        for x in range(len(mapTemp)):
            for y in range(len(mapTemp[i])):
                print(mapTemp[x][y], end=" ")
            print()


        sys.stdout = ogOutPut
        print("Type:",(i+1),"Map:", (j+1), ": completed")

