# Solved 06/05/2020
# CodeSignal
# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

def arrayChange(inputArray):
    # strictly increasing so 
    # core logic
    # move, check current> previous, 
    # if true move
    # if false, increment value + counter, check again loop
    # when true prev = current and move current pointer
    counter = 0
    prev = inputArray[0]
    for current in inputArray[1:]:
        if current > prev:
            prev = current
            continue
        else:
            while current <= prev:
                current += 1
                counter += 1
            prev = current
    return counter

my_arr = [1,1,1]
print(arrayChange(my_arr))