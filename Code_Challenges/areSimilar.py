# solved 06/03/20
# CodeSignal
# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

def areSimilar(a, b):
    # if you get to three differences anywhere along 
    # the way you can break and return False
    # create 2 dictionaries by looping through
    # if you finish the loop without errors
    # return true
    # if you finish the loop with 2 errors, AND
    # the dictionaries are the same 
    # return true
    # else 
    # return false
    # if you break early with more than 2 errors
    # return false
    # if you don
    errors = 0
    dicta = {}
    dictb = {}
    if len(a) != len(b):
        return False

    for i,j in zip(a,b):
        # check if they are the same
        if i != j:
            errors += 1
            if errors == 3:
                return False
        
        if dicta.__contains__(i):
            dicta[i] += 1
        else:
            dicta[i] = 1
        
        if dictb.__contains__(j):
            dictb[j] += 1
        else:
            dictb[j] = 1
    
    
    if dicta == dictb:
        return True
    else: 
        return False


# the muuuuuch simpler way from reading solutions:
def areSimilar2(a,b):
    return sorted(a) == sorted(b) and sum([i!=j for i,j in zip(a,b)]) <= 2


if __name__ == '__main__':
    # TESTS
    # same thing:
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(areSimilar(a,b))
    print(areSimilar2(a,b))
    print ('-'* 20)

    # one switch:
    a = [1, 2, 3]
    b = [2, 1, 3]
    print(areSimilar(a,b))
    print(areSimilar2(a,b))
    print ('-'* 20)

    # more than one switch
    a = [1, 1, 4]
    b = [2, 1, 3]
    print(areSimilar(a,b))
    print(areSimilar2(a,b))
    print ('-'* 20)

