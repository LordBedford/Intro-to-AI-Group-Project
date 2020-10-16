import random
from copy import copy, deepcopy

#Function to generate a map
def mapGen(rows,cols):
    #Initiate map with all 1 chars for regular unblocked cell
    map = [['1' for i in range(cols)] for j in range(rows)]

    for i in range(8):
        #Get coordinates for hard to traverse terrain area
        x_cord = random.randint(0,rows-1)
        y_cord = random.randint(0,cols-1)

        #Get range for the 31x31 area surrounding the coordinate. Fixes out of bounds errors
        row_start = x_cord - 15
        if x_cord-15 < 0:
            row_start = 0

        row_end = x_cord + 15
        if x_cord+15 > rows-1:
            row_end = rows-1

        col_start = y_cord - 15
        if y_cord-15 < 0:
            col_start = 0

        col_end = y_cord + 15
        if y_cord+15 > cols-1:
            col_end = cols-1

        #Fills in hard to traverse area
        for i in range(row_start, row_end+1):
            for j in range(col_start, col_end+1):
                if random.randint(1,2) == 1:
                    map[i][j] = '2'
    #Create rivers/highways
    #Get coordinates for river
    rivers = 0
    while rivers < 4:
        tempMap = deepcopy(map)
        river_x_cord = 0
        river_y_cord = 0
        #Determine what boundary river will start on
        #1 if on x-axis, 2 if on y-axis
        if random.randint(1,2) == 1:
            #top or bottom
            if random.randint(1,2) == 1:
                river_x_cord = rows-1
                river_y_cord = random.randint(0,cols-1)
            else: 
                river_x_cord = 0
                river_y_cord = random.randint(0,cols-1)
        else:
            #left or right
            if random.randint(1,2) == 1:
                river_y_cord = cols-1
                river_x_cord = random.randint(0,rows-1)
            else: 
                river_y_cord = 0
                river_x_cord = random.randint(0,rows-1)
        #Gets direction river will initially flow
        direction = ""
        if river_x_cord == rows-1:
            direction = "up"
        elif river_x_cord == 0:
            direction = "down"
        elif river_y_cord == cols-1:
            direction = "left"
        else: 
            direction = "right"

        tempxcord = river_x_cord
        tempycord = river_y_cord

        river_length = 0

        #Fill in river
        atBorder = 1
        while atBorder:
            #Traverse 20 spaces
            for j in range(20):
                #Up direction
                if direction == "up":
                    #Check if at border
                    if tempxcord - j <= 0 or tempMap[tempxcord-j][tempycord] == 'a' or tempMap[tempxcord-j][tempycord] == 'b':
                        atBorder = 0
                        break
                    #Check if hard to traverse terrain
                    if tempMap[tempxcord - j][tempycord] == '1':
                        tempMap[tempxcord - j][tempycord] = 'a'
                        river_length += 1
                    elif tempMap[tempxcord - j][tempycord] == '2':
                        tempMap[tempxcord - j][tempycord] = 'b'
                        river_length += 1
                #Down direction
                if direction == "down":
                    #Check if at border
                    if tempxcord + j >= rows-1 or tempMap[tempxcord+j][tempycord] == 'a' or tempMap[tempxcord+j][tempycord] == 'b':
                        atBorder = 0
                        break
                    #Check if hard to traverse terrain
                    if tempMap[tempxcord + j][tempycord] == '1':
                        tempMap[tempxcord + j][tempycord] = 'a'
                        river_length += 1
                    elif tempMap[tempxcord + j][tempycord] == '2':
                        tempMap[tempxcord + j][tempycord] = 'b'
                        river_length += 1
                # #Left direction
                if direction == "left":
                    #Check if at border
                    if tempycord - j <= 0 or tempMap[tempxcord][tempycord-j] == 'a' or tempMap[tempxcord][tempycord-j] == 'b':
                        atBorder = 0
                        break
                    #Check if hard to traverse terrain 
                    if tempMap[tempxcord][tempycord - j] == '1':
                        tempMap[tempxcord][tempycord - j] = 'a'
                        river_length += 1
                    elif tempMap[tempxcord][tempycord - j] == '2':
                        tempMap[tempxcord][tempycord - j] = 'b'
                        river_length += 1
                #Right direction
                if direction == "right":
                    #Check if at border
                    if tempycord + j >= cols-1 or tempMap[tempxcord][tempycord+j] == 'a' or tempMap[tempxcord][tempycord+j] == 'b':
                        atBorder = 0
                        break
                    #Check if hard to traverse terrain
                    if tempMap[tempxcord][tempycord + j] == '1':
                        tempMap[tempxcord][tempycord + j] = 'a'
                        river_length += 1
                    elif tempMap[tempxcord][tempycord + j] == '2':
                        tempMap[tempxcord][tempycord + j] = 'b'
                        river_length += 1
            #Gets coordinates for current position of river
            #Roll for new direction and change coordinates and path accordingly
            rand = random.randint(1,5)
            if direction == "up":
                if rand == 1:
                    direction = "left"
                    tempycord -= 20
                elif rand == 2:
                    direction = "right"
                    tempycord += 20
                else:
                    tempxcord -= 20
            elif direction == "down":
                if rand == 1:
                    direction = "left"
                    tempycord -= 20
                elif rand == 2:
                    direction = "right"
                    tempycord += 20
                else:
                    tempxcord += 20
            elif direction == "left":

                if rand == 1:
                    direction = "up"
                    tempxcord -= 20
                elif rand == 2:
                    direction = "down"
                    tempxcord += 20
                else:
                    tempycord -= 20
            elif direction == "right":
                if rand == 1:
                    direction = "up"
                    tempxcord -= 20
                elif rand == 2:
                    direction = "down"
                    tempxcord += 20
                else:
                    tempycord += 20
        if river_length >= 100:
            rivers+= 1
            map = deepcopy(tempMap)
    print(map)
    return map
mapGen(120,160)