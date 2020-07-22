# 072220
# CodeSignal
# https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm/solutions

def array_replace(inputArray, elemToReplace, substitutionElem):
    # loop through input array
    # if element = elemToReplace 
    # replace that element
    for index,i in enumerate(inputArray):
        if i == elemToReplace:
            inputArray[index] = substitutionElem
    return inputArray

