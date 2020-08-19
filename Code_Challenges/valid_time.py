def validTime(time):
    # split by the :
    # check if first value is between 0-24 
    # check second is between 0 and 59
    time = time.split(':')
    first = list(range(25))
    second = list(range(60))
    print(time)
    print(first,second)
    if inttime[0] in first and time[1] in second:
        return True
    return False

validTime("10:25")