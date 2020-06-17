# Solved 06/16/2020
# Codesignal
# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def isIPv4Address(inputString):
    # split by the dot
    # length of list should be 4
    # each item in the list should be of type int
    # each item in the list should be between 0 and 255
    
    a = len(inputString)
    if a>15 or a<7:
        return False
        
    output = inputString.split('.')
    if len(output) == 4:
        for i in output:
            # if there are leading zeroes in the input
            # then return false
            if len(i) > 1 and i[0] == '0':
                return False
            try:
                if int(i) < 256 and int(i) >= 0:
                    continue
                else:
                    return False
            except ValueError:
                return False
        return True
    else:
        return False