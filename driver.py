from MapMaker import *
from astarSearch import *
from MapCreator import *
#Drive class

run = True

map = MapMaker()
while(run):
   MapMaker.tick(map)



#mapTuple = MapCreator.mapGen(120,160)
#map = mapTuple[0]
#start = (0,0)
#goal = (100,100)
#print(a_star(map, start, goal))