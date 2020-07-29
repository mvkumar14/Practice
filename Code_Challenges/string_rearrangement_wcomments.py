def stringsRearrangement(inputArray):
    # the max difference between the first
    # string and the last string
    # should be less than the total number of
    # strings.
    
    # within the remaining set of the problem 
    # is it still possible to be false?
    # yeah if there is a gap of 2 at any point in between?
    # so the maximum distance is still good but there is one
    # place where the distance is 2. I just need to find it.
    
    # the largest problem here is going to be 
    # 10 items with length of 15 each.
    # the length doesn't matter
    # you have how many permutations of 10? (3,628,800)
    # so searching that possibility space 
    # for sequences, and then evaluating those sequences
    # is a naive solution to this problem.
    # could I do that in 4 seconds though? not sure.
    
    # how to find out the differences between the objects?
    # find all differences between every single one of the 
    # 10 objects . 
    # how can I then sequence them? 
    # I can draw out a graph? and maybe see if there is some
    # sequence of 
    # I can find 10 + 9 + 8 + 7 + ... + 1 distances between 
    # the strings. 
    # every single one has to have one that it is one away from.
    # them? the problem there is what if one item 
    # is one away from two objects, but isolated otherwise?
    # so when I use something then 
    
    # every item has to be one away from two other items at least, 
    # and there can't be repeats.
    
    # I can do a searching sort of thing where I look, but how would 
    # I do it in real life:
    
    for j in range(1,len(inputArray)):
        compare = inputArray[i]
        current_distance = distance(current,prev)
        if current_distance in distances:
            repeats = True
            break
        distances.append(current_distance)
    return dist_one(distances)
    
def metadata_check(distances):
    # this function returns true if the sequence
    # of numbers in the input array can be rearranged
    # such that the numbers are all a distance
    # of one away from the previous number in the sequence
    # false otherwise
    
    # there are two cases: 
    # one where there are repeats and
    # one where there are no repeats
    # if I get one with repeats, I could always 
    # do I have any sort of guarantee about the numbers
    # if there are repeats
    
    # ths difference between the max and the min has to be less
    # than or equal to the number of items in the list
    # (if you have a greater distance then one of the interor
    # differences will have to be greatere than 1)
    # if it is equal then the sorted set has to be strictly increasing
    # if it is less 
    
    # I can know what is in the set, and check for it instead
    # of the other way around?
    
    # you can look through sorted and check if
    # each value is one greater than the other
    # then you can look through the frequencies to make sure that they 
    # are one away from each other. 
    distances = sorted(distances)
    prev = distances[0]
    count = 1
    frequencies = []
    for i in distances:
        if i == prev:
            count += 1
            continue
        elif i == prev + 1:
            frequencies.append(count)
            count = 1
            continue
        else:
            return False
    
    prev = frequencies[0]
    for i in frequencies:
        if i == prev or i == prev + 1 or i == prev - 1:
            continue
        else:
            return False
    
    return True
    
    
    
    
    
    
    
def distance(a,b):
    # this function takes two strings, and tells you 
    # how many mutations it would take to get from one string to the other
    # the assumption is that both strings are the same size
    # there are no swaps allowed. Only mutations.
    count = 0 # counting the differences
    for i, j in zip(a,b):
        if i == j:
            continue
        else:
            count += 1
    return count
    
def distance_bool(a,b):
    # returns true if the distance 
    # between the strings is 1
    # and false otherwise.
    # remember we are looking for the exact amount of 
    count = 0
    for i, j in zip(a,b): 
        if i == j:
            continue
        else:
            if count == 1:
                return False
            else:
                count = 1
    return True
        

    
# this one would work for the perumtation method:
def sequence(inputArray):
    # this just checks if the sequence is true or false
    for i in range(1,len(inputArray)):
        if distance_bool(inputArray[i],inputArray[i-1]):
            continue
        else:
            return False
    return True
            
    

