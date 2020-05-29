# Solved 05/27/2020
# Hackerrank
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/

def isValid(s):
    # create a frequency count
    # if there are 3 plus frequencies return false
    # if there are two frequencies, but the difference in frequencies
    # is more than 1 return false
    # if there are two frequencies, and the larger one has only 1 value
    # and the larger one is only delta 1 from the smaller, return true
    # if there is only one frequency return true
    # in all other cases return false?

    if len(s) == 0:
        return "YES"

    frequencies = {}
    for char in s:
        if frequencies.__contains__(char):
            frequencies[char] += 1
            pass
        else:
            frequencies[char] = 1
            pass
    
    meta = {} # maybe I need a better name for this? its a frequency of frequencies.
    for key in frequencies:
        if meta.__contains__(frequencies[key]):
            meta[frequencies[key]] += 1
            pass
        else:
            meta[frequencies[key]] = 1
            pass
    
    num_freqs = len(meta)
    if num_freqs == 1:
        return "YES"
    elif num_freqs == 2:
        a, b = meta.items()
        big = max(a[0],b[0])
        small = min(a[0],b[0])
        
        if small == 1 and meta[small] == 1:
            return "YES"
        elif abs(a[0]-b[0]) == 1:
            if meta[big] == 1:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else:
        return "NO"