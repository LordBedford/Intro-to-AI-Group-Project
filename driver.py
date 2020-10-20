from MapMaker import *
from astarSearch import *
from MapCreator import *
import time
import statistics
#Drive class

#This runs all 50 files with all search algorithms and will compute its runtime
astar_runtime = []
weight_astar_runtime1 = []
weight_astar_runtime2 = []
uniform_runtime = []
astar_path = []
weight_path1 = []
weight_path2 = []
uniform_path = []
start_x = 0
start_y = 0
end_x = 0
end_y = 0
for i in range(5):
   for j in range(10):
      file = open("maps/map%s/map%s.txt" %(i, j), 'r')
      lines = file.readlines()
      start_x = lines[0].split()[0]
      start_y = lines[0].split()[1]
      end_x = lines[1].split()[0]
      end_y = lines[1].split()[1]
      tempCol = []
      desired_lines = lines[10::]
      for x in desired_lines:
             tempRows = []
             for y in x:
                    if not (y == ' ' or y == "\n"):
                           tempRows.append(y)
             tempCol.append(tempRows)

      start_time = time.time()
      a_star(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 120,160)
      astar_runtime.append(time.time() - start_time)

      start_time = time.time()
      weighted_a_star(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 1.25, 120,160)
      weight_astar_runtime1.append(time.time() - start_time)

      start_time = time.time()
      weighted_a_star(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 2, 120,160)
      weight_astar_runtime2.append(time.time() - start_time)

      #start_time = time.time()
      #uniform_cost_search(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 120,160)
      #uniform_runtime.append(time.time() - start_time)

      print("Map complete")

print("A* median runtime:", statistics.median(astar_runtime))
print("Weighted A*(1.25) runtime:", statistics.median(weight_astar_runtime1))
print("Weighted A*(2) runtime:", statistics.median(weight_astar_runtime2))
#print(statistics.median(uniform_runtime))

run = True
map = MapMaker()
while(run):
   MapMaker.tick(map)
