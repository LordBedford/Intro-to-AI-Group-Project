import math


# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position: (), parent: ()):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return '({0},{1})'.format(self.position, self.f)


# A*
# Takes in the map and start and goal points
def a_star(map, start, goal, x_max, y_max):
    # Lists for open and closed nodes
    open = []
    closed = []

    # Create a start and goal node
    start_node = Node(start, None)
    goal_node = Node(goal, None)

    # Add start node to open list
    open.append(start_node)

    count = 0
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
        # Map value at the current node
        parent_value = map[x][y]

        # Get 8 neighbors
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                     (x - 1, y - 1)]

        for next in neighbors:
            if next[0] < 0 or \
                    next[1] < 0 or \
                    next[0] >= x_max or \
                    next[1] >= y_max:
                continue
            neighbor = Node(next, current_node)

            # Map value of neighbor
            map_value = map[neighbor.position[0]][neighbor.position[1]]

            # Check if the node is impassable terrain
            if map_value == '0':
                continue

            # Check if the neighbor is in the closed list
            if neighbor in closed:
                continue

            # Using Diagonal distance heuristic

            # Both nodes are easy to traverse
            if (map_value == '1' and parent_value == '1') or \
                    (map_value == '1' and parent_value == '3') or \
                    (map_value == '3' and parent_value == '1') or \
                    (map_value == '3' and parent_value == '3'):

                # Moving vertically or horizontally
                if (neighbor.position == (x - 1, y)) or \
                        (neighbor.position == (x + 1, y)) or \
                        (neighbor.position == (x, y - 1)) or \
                        (neighbor.position == (x, y + 1)):

                    # Both nodes are on a highway
                    if map_value == '3' and parent_value == '3':
                        # Neighbor.g is current cost from start node + .25for 2 easy to traverse nodes
                        neighbor.g = current_node.g + .25
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h

                    # No highway
                    else:
                        # Neighbor.g is the current cost from start node + 1
                        neighbor.g = current_node.g + 1
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h

                #  Moving diagonally
                else:
                    # Neighbor.g is the current cost from start node + 1
                    neighbor.g = current_node.g + 1
                    neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2)
                    neighbor.f = neighbor.g + neighbor.h

            # One node is easy to traverse while one is hard
            elif (map_value == '1' and parent_value == '2') or \
                    (map_value == '1' and parent_value == '4') or \
                    (map_value == '2' and parent_value == '1') or \
                    (map_value == '2' and parent_value == '3') or \
                    (map_value == '3' and parent_value == '2') or \
                    (map_value == '3' and parent_value == '4') or \
                    (map_value == '4' and parent_value == '1') or \
                    (map_value == '4' and parent_value == '3'):

                # Moving vertically or horizontally
                if (neighbor.position == (x - 1, y)) or \
                        (neighbor.position == (x + 1, y)) or \
                        (neighbor.position == (x, y - 1)) or \
                        (neighbor.position == (x, y + 1)):

                    # Both nodes are on a highway
                    if (map_value == '4' and parent_value == '3') or \
                            (map_value == '3' and parent_value == '4'):
                        # Neighbor.g is current cost from start node + .375 for 1 hard and 1 regular cell
                        neighbor.g = current_node.g + .375
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h

                    # No highway
                    else:
                        # Neighbor.g is the current cost from start node + 1.5
                        neighbor.g = current_node.g + 1.5
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h

                else:
                    # Moving diagonally
                    # Neighbor.g is the current cost from start node + (sqrt(2)+sqrt(8))/2
                    neighbor.g = current_node.g + (math.sqrt(2) + math.sqrt(8)) / 2
                    neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2)
                    neighbor.f = neighbor.g + neighbor.h

            # Both nodes are hard to traverse
            elif (map_value == '2' and parent_value == '2') or \
                    (map_value == '2' and parent_value == '4') or \
                    (map_value == '4' and parent_value == '2') or \
                    (map_value == '4' and parent_value == '4'):

                # Moving vertically or horizontally
                if (neighbor.position == (x - 1, y)) or \
                        (neighbor.position == (x + 1, y)) or \
                        (neighbor.position == (x, y - 1)) or \
                        (neighbor.position == (x, y + 1)):

                    # Both nodes are on a highway
                    if map_value == '4' and parent_value == '4':
                        # Neighbor.g is current cost from start node + .5 for 2 hard cells
                        neighbor.g = current_node.g + .5
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h

                    else:
                        # Neighbor.g is the current cost from start node + 2
                        neighbor.g = current_node.g + 2
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h

                else:
                    # Moving Diagonally
                    # Neighbor.g is the current cost from start node sqrt(8)
                    neighbor.g = current_node.g + math.sqrt(8)
                    neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2)
                    neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            if add_open(open, neighbor):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


# Weighted A*
# Takes in the map and the start and goal points and a weight
def weighted_a_star(map, start, goal, weight, x_max, y_max):
    # Lists for open and closed nodes
    open = []
    closed = []

    # Create a start and goal node
    start_node = Node(start, None)
    goal_node = Node(goal, None)

    # Add start node to open list
    open.append(start_node)

    count = 0
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
        # Map value at the current node
        parent_value = map[x][y]

        # Get 8 neighbors
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                     (x - 1, y - 1)]

        for next in neighbors:
            if next[0] < 0 or \
                    next[1] < 0 or \
                    next[0] >= x_max or \
                    next[1] >= y_max:
                continue

            neighbor = Node(next, current_node)

            # Map value of neighbor
            map_value = map[neighbor.position[0]][neighbor.position[1]]

            # Check if the node is impassable terrain
            if map_value == '0':
                continue

            # Check if the neighbor is in the closed list
            if neighbor in closed:
                continue

            # Using Diagonal distance heuristic

            # Both nodes are easy to traverse
            if (map_value == '1' and parent_value == '1') or \
                    (map_value == '1' and parent_value == '3') or \
                    (map_value == '3' and parent_value == '1') or \
                    (map_value == '3' and parent_value == '3'):

                # Moving vertically or horizontally
                if (neighbor.position == (x - 1, y)) or \
                        (neighbor.position == (x + 1, y)) or \
                        (neighbor.position == (x, y - 1)) or \
                        (neighbor.position == (x, y + 1)):

                    # Both nodes are on a highway
                    if map_value == '3' and parent_value == '3':
                        # Neighbor.g is current cost from start node + .25for 2 easy to traverse nodes
                        neighbor.g = current_node.g + .25
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + (weight * neighbor.h)

                    # No highway
                    else:
                        # Neighbor.g is the current cost from start node + 1
                        neighbor.g = current_node.g + 1
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + (weight * neighbor.h)

                #  Moving diagonally
                else:
                    # Neighbor.g is the current cost from start node + 1
                    neighbor.g = current_node.g + 1
                    neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2)
                    neighbor.f = neighbor.g + (weight * neighbor.h)

            # One node is easy to traverse while one is hard
            elif (map_value == '1' and parent_value == '2') or \
                    (map_value == '1' and parent_value == '4') or \
                    (map_value == '2' and parent_value == '1') or \
                    (map_value == '2' and parent_value == '3') or \
                    (map_value == '3' and parent_value == '2') or \
                    (map_value == '3' and parent_value == '4') or \
                    (map_value == '4' and parent_value == '1') or \
                    (map_value == '4' and parent_value == '3'):

                # Moving vertically or horizontally
                if (neighbor.position == (x - 1, y)) or \
                        (neighbor.position == (x + 1, y)) or \
                        (neighbor.position == (x, y - 1)) or \
                        (neighbor.position == (x, y + 1)):

                    # Both nodes are on a highway
                    if (map_value == '4' and parent_value == '3') or \
                            (map_value == '3' and parent_value == '4'):
                        # Neighbor.g is current cost from start node + .375 for 1 hard and 1 regular cell
                        neighbor.g = current_node.g + .375
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + (weight * neighbor.h)

                    # No highway
                    else:
                        # Neighbor.g is the current cost from start node + 1.5
                        neighbor.g = current_node.g + 1.5
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + (weight * neighbor.h)

                else:
                    # Moving diagonally
                    # Neighbor.g is the current cost from start node + (sqrt(2)+sqrt(8))/2
                    neighbor.g = current_node.g + (math.sqrt(2) + math.sqrt(8)) / 2
                    neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2)
                    neighbor.f = neighbor.g + (weight * neighbor.h)

            # Both nodes are hard to traverse
            elif (map_value == '2' and parent_value == '2') or \
                    (map_value == '2' and parent_value == '4') or \
                    (map_value == '4' and parent_value == '2') or \
                    (map_value == '4' and parent_value == '4'):

                # Moving vertically or horizontally
                if (neighbor.position == (x - 1, y)) or \
                        (neighbor.position == (x + 1, y)) or \
                        (neighbor.position == (x, y - 1)) or \
                        (neighbor.position == (x, y + 1)):

                    # Both nodes are on a highway
                    if map_value == '4' and parent_value == '4':
                        # Neighbor.g is current cost from start node + .5 for 2 hard cells
                        neighbor.g = current_node.g + .5
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + (weight * neighbor.h)

                    else:
                        # Neighbor.g is the current cost from start node + 2
                        neighbor.g = current_node.g + 2
                        neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                                neighbor.position[1] - goal_node.position[1]) ** 2)
                        neighbor.f = neighbor.g + (weight * neighbor.h)

                else:
                    # Moving Diagonally
                    # Neighbor.g is the current cost from start node sqrt(8)
                    neighbor.g = current_node.g + math.sqrt(8)
                    neighbor.h = math.sqrt((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2)
                    neighbor.f = neighbor.g + (weight * neighbor.h)

            # Check if neighbor is in open list and if it has a lower f value
            if add_open(open, neighbor):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


def add_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True
