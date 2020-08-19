def spiralNumbers(n):
    # create blank output matrix
    matrix = []
    for _ in range(n):
        matrix.append([0]*n)
    
    # A spiral pattern contains n+n-1 pieces
    # where n is the length of a side (the input value to the funciton)
    # you can count this by starting from the center
    # or starting from the top. lets start from the top
    # you strart with n (for example 5)
    # the first edge is going to be of size n 
    # and starts from the top left and goes to the top right
    # then you have two edges of size n-1 
    # (6-9) and (10-13) both containing 4 (= 5-1) 
    # numbers in the edge
    # then two edges of size n-2 and so on 
    # until you get two edges of size 1
    # in effect you have the range [1 - n-1] doubled + 1
    # "pieces" or "edges" to the spiral.
    # another way to represent this is:
    # (n-1)*2 + 1 or (n)*2 - 1
    
    # all this is to say: there is a deterministic way to figure out
    # the number of edges. We can use this to determine how many times
    # we need to run an exterior for loop
    # the pattern of edges is also consistent 
    # and it is dependent on the current value of the exterior loop 
    # (assuming we loop through a range) so we can create
    # an interior for loop that loops through each element of an edge
    # correctly as well
    
    # x = row
    # y = column
    # starting top left positive x is right
    # positive y is down
    
    x = -1 # column
    y = 0 # row
    counter = 1
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    for i in range(n+n-1):
        # the pattern for the number of interior loop is
        # n,n-1,n-1,n-2,n-2 ... 1,1
        # we can get this pattern using the floor division 
        # operator on a range of numbers from 2n -> 0 
        for j in range((n+n-i)//2):
            x += dx[i%4]
            y += dy[i%4]
            matrix[y][x] = counter
            counter += 1
    return matrix
            

print(spiralNumbers(4))  