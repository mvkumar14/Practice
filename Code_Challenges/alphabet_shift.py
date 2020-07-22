
def alphabeticShift(inputString):
    shift = 1
    outputstr = ''
    for i in inputString:
        print("_____CHARACTER______")
        print(ord(i))
        print(chr(ord(i)+shift))
        print((ord(i)+shift)%26)
        print(((ord(i)+shift)%26)+97)
        print(chr(((ord(i)+shift) % 26) + 97))
        outputstr += chr(((ord(i)+shift) % 26) + 97)
    return outputstr

alphabeticShift('crazy')