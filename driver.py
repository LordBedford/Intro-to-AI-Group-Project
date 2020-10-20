#Peter Marchese

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
seq_runtime = []

astar_path = []
weight_path1 = []
weight_path2 = []
uniform_path = []
seq_path = []

astar_expanded = []
weight_expanded = []
weight2_expanded = []
uniform_expanded = []
seq_expanded = []

start_x = 0
start_y = 0
end_x = 0
end_y = 0

tempCol = []
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
      aTemp = a_star(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 120,160)
      astar_path.append(len(aTemp[0]))
      astar_runtime.append(time.time() - start_time)
      astar_expanded.append(aTemp[1])

      start_time = time.time()
      w1Temp = weighted_a_star(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 1.25, 120,160)
      weight_path1.append(len(w1Temp[0]))
      weight_astar_runtime1.append(time.time() - start_time)
      weight_expanded.append(w1Temp[1])

      start_time = time.time()
      w2temp = weighted_a_star(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 2, 120,160)
      weight_path2.append(len(w2temp[0]))
      weight_astar_runtime2.append(time.time() - start_time)
      weight2_expanded.append(w2temp[1])

      start_time = time.time()
      sTemp = sequential_heuristic(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 1.25, 2, 120,160)
      seq_path.append(len(sTemp[0]))
      seq_runtime.append(time.time() - start_time)
      seq_expanded.append(sTemp[1])

# start_time = time.time()
# uTemp = uniform_cost_search(tempCol, (int(start_x), int(start_y)), (int(end_x), int(end_y)), 120,160)
# uniform_path.append(len(uTemp[0]))
# uniform_runtime.append(time.time() - start_time)
# uniform_expanded.append(uTemp[1])

print("A* median runtime:", statistics.median(astar_runtime))
print("Weighted A*(1.25) runtime:", statistics.median(weight_astar_runtime1))
print("Weighted A*(2) runtime:", statistics.median(weight_astar_runtime2))
#print("Uniform median runtime:", statistics.median(uniform_runtime))
print("////////////////////////////////////////////////")
print("A* median length:", statistics.median(astar_path))
print("Weighted A*(1.25) length:", statistics.median(weight_path1))
print("Weighted A*(2) length:", statistics.median(weight_path2))
#print("Uniform median length:", statistics.median(uniform_path))
print("////////////////////////////////////////////////")
print("A* median expanded median nodes:", statistics.median(astar_expanded))
print("Weighted A*(1.25) median expanded nodes:", statistics.median(weight_expanded))
print("Weighted A*(2) median expanded nodes:", statistics.median(weight2_expanded))
#print("Uniform median expanded nodes:", statistics.median(uniform_expanded))
print("////////////////////////////////////////////////")
print("Sequential median runtime:", statistics.median(seq_runtime))
print("Sequential median length:", statistics.median(seq_path))
print("Sequential median expanded nodes:", statistics.median(seq_expanded))

run = True
map = MapMaker()
while(run):
   MapMaker.tick(map)
