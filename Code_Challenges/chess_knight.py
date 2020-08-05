def chessKnight():
    column = ord(cell[0])-96 (should get 1-8)
    row = int(cell[1])
    first = [[i,j] for i in [-1,1] for j in [-2,2]]
    second = [[j,i] for i in [-1,1] for j in [-2,2]]
    both = first.extend(second)
    count = 0
    for i,j in both:
        check_row = row + i
        check_column = column + j
        if inside_board(check_row,check_column):
            count += 1
    return count

def inside_board(x,y):
    # if x is between 1 and 8 and 
    # y is between 1 and 8 then true
    # else false
    if x >=1 and x <= 8 and y>= 1 and y<=8:
        return True
    return False


chessKnight()