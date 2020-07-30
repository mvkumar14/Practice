def newRoadSystem(rr):
    # As long as the row and the
    # column have the same number of trues
    # then it is good.
    rows = [0]*len(rr)
    columns = [0]*len(rr)
    for index1, i in enumerate(rr):
        rows[index1] = sum(i)
        for index2, j in enumerate(i):
            if j:
                columns[index2] += 1
    
    for i,j in zip(rows,columns):
        if i == j:
            continue
        else:
            return False
    
    return True
            