
from string import ascii_letters

def is_anagram(a,b):
    # input filtering

    # remove punctuation, spaces, and make lower in one operation
    tmp = ""
    a_count = 0
    b_count = 0
    for i in a: 
        if i in ascii_letters:
            tmp += i.lower()
            a_count += 1
    a = tmp

    tmp = ''
    for i in b:
        if i in ascii_letters:
            tmp += i.lower()
            b_count += 1
    b = tmp

    if a_count != b_count:
        return False
    
    # take either word, and
    # loop through the word storing letters 
    # in a dictionary

    dict_a = {}
    dict_b = {}
    for i in a:
        try:
            dict_a[i] += 1
        except KeyError:
            dict_a[i] = 1

    for i in b:
        try:
            dict_b[i] +=1
        except KeyError:
            dict_b[i] = 1
    
    if len(dict_a) != len(dict_b):
        return False

    for i in dict_a:
        try:
            if dict_a[i] != dict_b[i]:
                return False 
        except KeyError:
            return False

    return True
    
def is_anagram_2(a,b):
    # remove spaces:
    a = ''.join(a.split())
    b = ''.join(b.split())

    # make both lower
    a = a.lower()
    b = b.lower()
    
    # simple check 
    if len(a) != len(b):
        return False
    

    # take either word, and for every letter, 
    # loop through the other word. 
    # if you find that letter:
        # delete that letter from the word
        # continue
    # if you don't find that letter
        # return False

    for i in a:
        found = False
        for j in b:
            if i == j:
                b.replace(j,'',1)
                found = True
                continue
        if found is False:
            return False 

    return True   
    
    
print(is_anagram('test','Ettt'))