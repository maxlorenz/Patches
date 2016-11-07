from math import sqrt

class Patch(object):
    def __init__(self, number, x, y):
        self.number = number
        self.origin = { 'x': x, 'y': y }
        self.position = { 'x': x, 'y': y }

        self.x_neighbors = []
        self.y_neighbors = []


    def add_x_neighbor(self, patch):
        self.x_neighbors.append(patch)

    def add_y_neighbor(self, patch):
        self.y_neighbors.append(patch)


    def __distance__(self, pos_a, pos_b):
        delta_x = pos_a['x'] - pos_b['x']
        delta_y = pos_a['y'] - pos_b['y']

        return abs(2*delta_x + delta_y)

    def __distance_from_x_neighbors__(self):
        distances = [ self.__distance__(self.position, x.position) for x in self.x_neighbors ]
        return sum(distances)

    def __distance_from_y_neighbors__(self):
        distances = [ self.__distance__(self.position, y.position) for y in self.y_neighbors ]
        return sum(distances)

    def __distance_from_origin__(self):
        return self.__distance__(self.position, self.origin)

    def get_distance(self):
        distance_x = self.__distance_from_x_neighbors__()
        distance_y = self.__distance_from_y_neighbors__()
        distance_origin = self.__distance_from_origin__()

        distance_total = distance_x + distance_y + distance_origin
        default_total = 2*len(self.x_neighbors) + len(self.y_neighbors)
        return distance_total - default_total
