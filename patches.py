from math import sqrt

class Patch(object):
    def __init__(self, number, column, row, height=1, width=1):
        self.number = number
        self.origin = {  'row': row, 'column': column }
        self.position = {  'row': row, 'column': column }

        self.height = height
        self.width = width

        self.x_neighbors = []
        self.y_neighbors = []

    def __distance(self, pos_a, pos_b):
        delta_x = pos_a['column'] - pos_b['column']
        delta_y = pos_a['row'] - pos_b['row']

        return sqrt((delta_x * self.width)**2 + (delta_y * self.height)**2)

    def __distance_from_x_neighbors(self):
        distances = [ self.__distance(self.position, x.position) for x in self.x_neighbors ]
        return sum(distances)

    def __distance_from_y_neighbors(self):
        distances = [ self.__distance(self.position, y.position) for y in self.y_neighbors ]
        return sum(distances)

    def __distance_from_origin(self):
        return self.__distance(self.position, self.origin)

    def add_x_neighbor(self, patch):
        self.x_neighbors.append(patch)

    def add_y_neighbor(self, patch):
        self.y_neighbors.append(patch)

    def get_distance(self):
        distance_x = self.__distance_from_x_neighbors()
        distance_y = self.__distance_from_y_neighbors()
        distance_origin = self.__distance_from_origin()

        distance_total = distance_x + distance_y + distance_origin
        default_total = len(self.x_neighbors) + len(self.y_neighbors)
        return distance_total - default_total
