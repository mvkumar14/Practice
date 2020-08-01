def buildPalindrome(st):
    # if its a palindrome return the length of the string
    # if it isn't a palindrome then...
    # go backwards... as soon as you find a palindrome
    # then create a new string that adds
    # the letters you see from that point onwards
    
    #check if original is palindrome
    if check_palindrome(st):
        return st

    # starting from the beginning
    # check the "rest" of the string
    # if it is a palindrome then add what you have so
    # far in reverse order to the end
    # if it isn't continue
    
    add_st = ''
    beginning = st[0]
    for index in range(1:len(st)):
        end = st[index:]
        if check_palindrome(end):
            return st + beginning[::-1]
        else:
            beginning += st[index] 
    return st + beginning[::-1] 

def check_palindrome(st):
    # start from the beginning 
    # and the end
    # and check that the characters 
    # match to the middle character
    # if there is an even number of characters
    # you can just split the string and check that
    # the first and last halves match
    # if there is an odd number then you can still 
    # split but there are some checks involved?
    if len(st)== 0 or len(st) == 1:
        return False

    mid = len(st)//2
    
    if len(st) % 2 == 0: 
        # if even number of letter
        first = st[0:mid]
        last = st[mid:]
    else:
        # if there is an odd number of letters
        first = st[0:mid]
        last = st[mid+1:]
        
    last_rev = last[::-1]
    if first == last_rev:
        return True
    else:
        return False

data = 'ababab'
buildPalindrome(data)