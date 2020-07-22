def minesweeper(matrix):
    # make a border 
    # have an algorithm that checks the adjacent
    # tiles for a mine, excluding corner adjacency
    
    # or you have to use try except and address the 
    
    # Putting a border in:
    new_matrix = []
    new_matrix.append([False]*(len(matrix[0])+2))
    temp = []
    for i in matrix:
        print(i)
        temp = []
        temp.append(False)
        temp.extend(i)
        temp.append(False)
        new_matrix.append(temp)
    new_matrix.append([False]*(len(matrix[0])+2))
    # Now we have to check the inner matrix's surroundings 
    output_matrix = []
    height = len(new_matrix)
    width = len(new_matrix[0])
    # print(f"new_matrix = {new_matrix}")
    # print(f"width={width}")
    # print(range(1,width-1))
    # print(temp)
    for i in range(1,height-1):
        row = []
        for j in range(1,width-1):
            #check the four edges
            #add value to output 
            num_mines = 0
            if new_matrix[i-1][j-1]== True:
                num_mines += 1
            if new_matrix[i-1][j]==True:
                num_mines += 1
            if new_matrix[i-1][j+1]==True:
                num_mines += 1
            if new_matrix[i][j-1]==True:
                num_mines += 1
            # if new_matrix[i][j]==True:
            #     num_mines += 1
            if new_matrix[i][j+1]==True:
                num_mines += 1
            if new_matrix[i+1][j-1]==True:
                num_mines += 1
            if new_matrix[i+1][j]==True:
                num_mines += 1
            if new_matrix[i+1][j+1]==True:
                num_mines += 1
            row.append(num_mines)
        output_matrix.append(row)
    return output_matrix


test = [[True,False,False], 
 [False,True,False], 
 [False,False,False]]

# print("-------------")
# print("TEST 1")
# print(minesweeper(test))

# test = [[False,False,False],[False,False,False]]

# print("-------------")
# print("TEST 2")
# print(minesweeper(test))

print(-test[0][1])