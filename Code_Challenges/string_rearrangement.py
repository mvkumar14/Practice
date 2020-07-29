def stringsRearrangement(inputArray):
    compare = inputArray[0]
    distances = []
    for i in inputArray:
        current_distance = distance(compare,i)
        distances.append(current_distance)
    return metadata_check(distances)
    
def metadata_check(distances):
    distances = sorted(distances)
    prev = distances[0]
    count = 0
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

    frequencies.append(count)
    prev = frequencies[0]

    if len(frequencies) == 1:
        return False

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
    # remember we are looking for a distance of exactly 1 
    # zeros aren't allowed
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


# data = ["zzzzab", 
#  "zzzzbb", 
#  "zzzzaa"]

# print(stringsRearrangement(data))
            
    

