## Sudoku Solver (v1)
This project contains a simple sudoku solver. 
The minimum number of iterations is pretended to be achieved.

### Sudoku rules
1. Sudoku is a 9-by-9 grid (81 boxes in total) to fill with numbers between 1 and 9.
2. Some boxes are initially filled with "key numbers".
3. The grid is formed by 9 3-by-3 regions. These regions will be named as "subgrids".
3. **Goal**: Fill every box, so each column, row and region contains every number
   between 1 and 9 JUST ONE TIME.
   
### Proposed solution
Two steps are executed in a loop that ends when the Sudoku is fullfilled.
 _(In this first version, just one-solution Sudokus can be solved)_.

- _First step:_ Check for boxes with a unique candidates, and fill them. 
If at least one box has been filled, a subsequent iteration will be executed to solve 
 new possible "straightforward" candidates.

- Second step: Check inside the subgrid of each box to make sure that a particular candidate
has a unique possible position.

### TODO
- Improve the algorithm to deal with multiple-solution Sudokus.
- Optimization
