def avoidObstacles(inputArray):
    b = sorted(inputArray)
    # easiest method:
    # try 1 , try 2, try 3 so on and so forth
    counter = 2
    prev = b[0]
    denoms = []
    for i in b[1:]: 
        if i == prev + 1:
            counter += 1
        else:
            if counter in denoms:
                counter = 2
            else:
                denoms.append(counter)
                counter = 2
        prev = i
    print(denoms)
    return denoms

test_arr = [5,6,9,3,7]
avoidObstacles(test_arr)