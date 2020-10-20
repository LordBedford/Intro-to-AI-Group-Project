from MapMaker import *
from astarSearch import *
from MapCreator import *
#Drive class

run = True

map = MapMaker()
while(run):
   MapMaker.tick(map)



mapTuple = MapCreator.mapGen(120,160)
map = mapTuple[0]
start = (11,157)
goal = (119,12)
print(a_star(map, start, goal))