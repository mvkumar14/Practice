# Solved 05/28/2020 
# Hackerrank
# https://www.hackerrank.com/challenges/sherlock-and-anagrams
# In class at Lambda School

def sherlockAndAnagrams(s):
    # slice up substrings and check if substrings are anagrams
    # you have to slice by different sizes of substrings,
    # and you have to loop through to find every combination of 
    # substrings to check. within the main string. 
    # 1) Get substrings 
    # 2) Check substrings


    # Main loop increase size of substring window from 1-> n-1
    # For each substring size, ....
        # find every combination of substrings of that size using a 
        # sliding window. check s[0] vs s[1],s[2],s[3]  ....
        # check s[0:1],s[1:2],s[2:3] (moving both end and beginning of window up by 1)
        # until the end of the window is = end 
        # then check s[1] against s[2],s[3] ...

    # The way to check anagrams can be by putting the sorted
    # version of the substring into a frequency count dictionary.
    # This way you just need to find out the number of possible combinations
    # of a 
    substring_length = 1
    frequency = {}
    last = len(s)-1
    while substring_length < len(s):
        start_window = 0
        
        while True:
             # move pointer from beginning to end when you hit end break loop
            end_window = start_window + substring_length
            substring = s[start_window:end_window]
            substring = "".join(sorted(substring))
            if frequency.__contains__(substring):
                frequency[substring] += 1
            else:
                frequency[substring] = 1
            start_window += 1
            if end_window == len(s):
                break
        substring_length += 1
    count = 0
    for i in frequency.values():
        count += i*(i-1)/2
    return int(count)

sherlockAndAnagrams('ifailuhkqq')
sherlockAndAnagrams('kkkk')