"""
Author: Fran Moreno
GitHub: https://github.com/Franm99
Date:   10/16/2021
"""

# SUDOKU GAME SOLVER
# Rules:
# 1. Sudoku is a 9-by-9 grid (81 boxes in total) to fill with numbers between 1 and 9.
# 2. Some boxes are initially filled with "key numbers".
# 3. The grid is formed by 9 3-by-3 regions.
# 3. Goal: Fill every box, so each column, row and region contains every number
#    between 1 and 9 JUST ONE TIME.

import numpy as np
import time

from sudokus_to_solve import hard1 as grid_list  # Change the imported empty sudoku, but not it alias name


class Sudoku:
    def __init__(self, grid: np.array, solved: bool = False):
        self.grid = np.copy(grid)
        self.solved = solved
        self._dims = (9, 9)
        self._iters = 0

        # Array of lists to save candidate numbers
        self._candidates = np.empty(self._dims, dtype=object)
        for i in range(self._dims[0]):
            for j in range(self._dims[1]):
                self._candidates[i, j] = []

    def solve(self):
        start = time.time()
        iters, iters_limit = 0, 100
        while (not self.solved) and (iters < iters_limit):
            # 1. Update candidates
            self.__update_candidates()
            self.__search_in_group()
            if self.__get_remaining_boxes() == 0:
                self.solved = True
                print("Sudoku solved in {} iterations!".format(self._iters))
                print(self.grid)
            iters += 1
        end = time.time() - start
        if iters == iters_limit:
            print("Can not solve this Sudoku... Maybe multiple solutions exists :/")
        print("Time elapsed: {}".format(end))

    def __get_remaining_boxes(self) -> int:
        return np.count_nonzero(self.grid == 0)

    def __update_candidates(self):
        """ Loop over the grid searching candidates. """
        at_least_one = True
        while at_least_one:
            self._iters += 1
            at_least_one = False
            for ix, iy in np.ndindex(self.grid.shape):
                if self.grid[ix, iy] != 0:
                    continue

                row = self.grid[ix, :]
                col = self.grid[:, iy]
                sx, sy = (ix//3)*3, (iy//3)*3
                subgrid = self.grid[sx:sx+3, sy:sy+3]

                # Search for candidates
                candidates = [i for i in range(1, 10)
                              if ((i not in row) and (i not in col) and (i not in subgrid.flatten()))]

                if len(candidates) == 1:  # If it only exists 1 candidate, fill the box with it
                    self.grid[ix, iy] = candidates.pop()
                    at_least_one = True
                else:
                    self._candidates[ix, iy] = candidates

    def __search_in_group(self):
        self._iters += 1
        for ix, iy in np.ndindex(self.grid.shape):
            if self.grid[ix, iy] != 0:
                continue
            sx, sy = (ix // 3) * 3, (iy // 3) * 3
            subgrid_candidates = self._candidates[sx:sx + 3, sy:sy + 3]
            current_candidates = self._candidates[ix, iy]
            for c in current_candidates:
                num = 0
                for candidates in subgrid_candidates.flatten():
                    if c in candidates:
                        num += 1
                if num == 1:
                    self.grid[ix, iy] = c


if __name__ == '__main__':

    starting_grid = np.array(grid_list)
    print("Sudoku to solve: ")
    print(starting_grid)

    sudoku = Sudoku(starting_grid)
    sudoku.solve()
