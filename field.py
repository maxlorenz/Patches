import random
from patches import Patch

class Board(object):
    def __create_patches__(self):
        for row_number in range(self.rows):
            row = []

            for column_number in range(self.columns):
                number = row_number * self.columns + column_number + 1
                patch = Patch(number, row_number, column_number)
                row.append(patch)

            self.patches.append(row)

    def __find_neighbors__(self, patch, row, column):
        if column > 0:
            patch.add_y_neighbor(self.patches[row][column - 1])
        if column < self.columns - 1:
            patch.add_y_neighbor(self.patches[row][column + 1])

        if row > 0:
            patch.add_x_neighbor(self.patches[row - 1][column])
        if row < self.rows - 1:
            patch.add_x_neighbor(self.patches[row + 1][column])

    def __add_neighbors__(self):
        for row in range(self.rows):
            for column in range(self.columns):
                patch = self.patches[row][column]
                self.__find_neighbors__(patch, row, column)


    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.patches = []
        self.last_swap = []

        self.__create_patches__()
        self.__add_neighbors__()

    def get_cost(self):
        distances = [ 
            patch.get_distance() 
            for row in self.patches 
            for patch in row ]

        return sum(distances)

    def swap(self, pos_a, pos_b):
        patch_a = self.patches[pos_a['x']][pos_a['y']]
        patch_b = self.patches[pos_b['x']][pos_b['y']]

        patch_a.position, patch_b.position = patch_b.position, patch_a.position
        self.last_swap = [ pos_a, pos_b ]

    def unswap(self):
        self.swap(self.last_swap[1], self.last_swap[0])

    def __random_position__(self):
        return {
            'x': random.randint(0, self.rows - 1),
            'y': random.randint(0, self.columns - 1) }

    def swap_random(self):
        pos_a = self.__random_position__()
        pos_b = self.__random_position__()

        self.swap(pos_a, pos_b)