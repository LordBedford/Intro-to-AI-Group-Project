import random


# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


# A*
def a_star(map):
    # Lists for open and closed nodes
    open = []
    closed = []

    # Create a start and goal node
    start = (start_x_cord, start_y_cord)
    end = (end_x_cord, end_y_cord)
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add start node to open list
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Sort open list to find lowest cost node and add it it closed list
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            # Return reversed path
            return path[::-1]

        (x, y) = current_node.position
        # Get 8 neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]

        for next in neighbors:
            map_value = map.get(next)
            # Check if the node is impassable terrain
            if (map_value == '0'):
                continue

            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if (neighbor in closed):
                continue
            # Manhattan distance heuristic
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(
                neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if (add_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


# Weighted A*
def weighted_a_star(map):
    # Lists for open and closed nodes
    open = []
    closed = []

    # define weight for w >= 1
    weight = 1.2

    # Create a start and goal node
    start = (start_x_cord, start_y_cord)
    end = (end_x_cord, end_y_cord)
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add start node to open list
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Sort open list to find lowest cost node and add it it closed list
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            # Return reversed path
            return path[::-1]

        (x, y) = current_node.position
        # Get 8 neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]

        for next in neighbors:
            map_value = map.get(next)
            # Check if the node is impassable terrain
            if (map_value == '0'):
                continue

            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if (neighbor in closed):
                continue
            # Manhattan distance heuristic
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(
                neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + (weight * neighbor.h)
            # Check if neighbor is in open list and if it has a lower f value
            if (add_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


def add_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True
