import MapCreator
import numpy as np



for i in range(10):
    temp = MapCreator.mapGen(120, 160)
    tempMap = temp[0]
    filenumber = str(i)
    savefile = open("maps/map%s.txt" % filenumber, 'w')
    np.savetxt(savefile, tempMap, fmt='%s')
    print("Map", (i+1), ": completed")
