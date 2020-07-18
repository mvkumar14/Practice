# Solved 07172020
# Codesignal.com

# TODO
# Write unittest for this file
# explore reducing the input set by
# using prime numbers.

def avoidObstacles(inputArray):
    # start with 2 and see if every
    # numbber is divisible by 2
    # if it is then move 2 to 3
    # if every number is not divisible by 
    # the number you are on
    # then that number is min_jumps
    # ------------------
    # Possible room for optimization
    # start at higher and higher numbers
    # you can reduce this problem further by 
    # analyzing the prime factors of the items
    # in the set, but I'll explore that later.
    
    inputArray = sorted(inputArray)
    current_jumps = 2
    while True:  # until you find an answer which will break the loop
        flag = True
        for val in inputArray:   # check if every value is divisible by the current min_jumps
            if val % current_jumps == 0:  # its divisible
                flag = False
                current_jumps += 1
                break
        if flag:  # aka if I get through the whole list
            return current_jumps  # which will break the while loop     