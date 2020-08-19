import numpy as np

def sudoku(grid):
    # slice the grid 
    # do a len(set()) on the slice
    # if any of the slices return false
    # return false
    # else return true
    for i in range(3):
        for j in range(3):
            print(grid[i*3:(i*3+3),j*3:(j*3+3)])

grid = np.array([[1,3,2,5,4,6,9,8,7], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]])
my_list = []
for i in grid[0:3,0:3]:
    for j in i:
        my_list.append(j)
print([j for i in grid[0:3,0:3] for j in i])
# sudoku(grid)