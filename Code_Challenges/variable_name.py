
# 072220
# CodeSignal
# https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

# TODO figure out the following
# something weird in this one was that if I did all the 
# checks together (if i in alpha or numeric or ['_'])
# it wouldn't filter out -'s. 

from string import ascii_letters as alpha

def variable_name(name):
    numeric = ["1","2","3","4","5","6","7","8","9","0"]
    if name[0] in numeric:
        return False
    for i in name:
        if i in alpha:
            continue 
        elif i in numeric:
            continue
        elif i == "_":
            continue
        else: 
            return False
    return True


print(variable_name("qq-q"))