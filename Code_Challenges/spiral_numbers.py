def spiralNumbers(n):
    matrix = []
    for _ in range(n):
        matrix.append([0]*n)
    # keep i constant change j (positivley)
    # until you hit the edge or a number
    # that isn't 0
    
    # then switch keep j constant and 
    # change i (positivley)
    
    # switch keep i constant change j (negativley)
    
    # keep j constant switch i (positivley)
    
    row = 0
    column = 0
    additions = [(0,1),(1,0),(0,-1),(-1,0)]
    num_switches = 0
    for i in range(1,n*n+1):
        try:
            access = matrix[row][column]
            if row < 0 or column < 0 or matrix[row][column] != 0:
                # move back to last location
                row -= additions[num_switches%4][0]
                column -= additions[num_switches%4][1]
                # iterate num_switches
                num_switches += 1
                # move in next direction
                row += additions[num_switches%4][0]
                column += additions[num_switches%4][1]
                # fill the matrix
                matrix[row][column] = i
            else:
                matrix[row][column] = i
        except IndexError:
            # move back to last location
            row -= additions[num_switches%4][0]
            column -= additions[num_switches%4][1]
            # iterate num_switches
            num_switches += 1
            # move in next direction
            row += additions[num_switches%4][0]
            column += additions[num_switches%4][1]
            # fill the matrix
            matrix[row][column] = i
        
        #strategy to iterate row or column
        row += additions[num_switches%4][0]
        column += additions[num_switches%4][1]
    return matrix

print(spiralNumbers(4))