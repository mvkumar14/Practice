import numpy as np

import numpy as np

def differentSquares(matrix):
    # you need to check every matrix and see if
    # if it is unique.
    seen = []
    matrix = np.array(matrix)
    count = 0
    flag = True
    for row in range(0,len(matrix)-1):
        for column in range(0,len(matrix[0])-1):
            first = list(matrix[row:row+2,column])
            second = list(matrix[row:row+2,column+1])
            first.extend(second)
            if first in seen:
                continue
            else:
                seen.append(first)
                count += 1
    return count



data = [[1,2,1], 
 [2,2,2], 
 [2,2,2], 
 [1,2,3], 
 [2,2,1]]

print(differentSquares(data))
