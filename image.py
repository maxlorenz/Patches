from random import randint
from patches import Patch

class Image(object):
    def __init__(self, rows, columns, patch_width=1, patch_height=1):
        self.rows = rows
        self.columns = columns
        self.patches = []
        self.last_swap = []

        self.patch_width = patch_width
        self.patch_height = patch_height

        self.__create_patches()
        self.__add_neighbors()

    def __create_patches(self):
        for row_number in range(self.rows):
            row = []

            for column_number in range(self.columns):
                number = row_number * self.columns + column_number + 1
                patch = Patch(number, column_number, row_number, width=self.patch_width, height=self.patch_height)
                row.append(patch)

            self.patches.append(row)

    def __find_neighbors(self, patch, position):
        row = position['row']
        column = position['column']

        if column > 0:
            patch.add_x_neighbor(self.patches[row][column - 1])
        if column < self.columns - 1:
            patch.add_x_neighbor(self.patches[row][column + 1])

        if row > 0:
            patch.add_y_neighbor(self.patches[row - 1][column])
        if row < self.rows - 1:
            patch.add_y_neighbor(self.patches[row + 1][column])

    def __random_position(self):
        return {
            'row': randint(0, self.rows - 1),
            'column': randint(0, self.columns - 1)
        }

    def __add_neighbors(self):
        for patch in self.all_patches():
            self.__find_neighbors(patch, patch.position)

    def all_patches(self):
        return([ patch for row in self.patches for patch in row ])       
        
    def get_total_distances(self):
        return sum([ patch.get_distance() for patch in self.all_patches() ]) / len(self.patches)

    def swap(self, pos_a, pos_b):
        patch_a = self.patches[pos_a['row']][pos_a['column']]
        patch_b = self.patches[pos_b['row']][pos_b['column']]

        patch_a.position, patch_b.position = patch_b.position, patch_a.position
        self.last_swap = [ pos_a, pos_b ]

    def undo_swap(self):
        self.swap(self.last_swap[1], self.last_swap[0])

    def swap_random(self):
        pos_a = self.__random_position()
        pos_b = self.__random_position()

        self.swap(pos_a, pos_b)