# Solved 05/26/2020 
# HackerRank 
# https://www.hackerrank.com/challenges/alternating-characters

def alternatingCharacters(s):
    output = []
    for letter_string in s[1:]:
        # If we are ever going to have single letters or no letters?
        # str_len = len(letter_string)
        # if str_len == 0 or str_len == 1:
        #     output.append(0)
        
        prev = letter_string[0] #if case sensitive/ mixed case do a .lower here
        del_count = 0
        for letter in letter_string[1:]:
            if letter == prev:
                del_count += 1
            else:
                prev = letter
        output.append(del_count)
    return output

test_1 = 'AAAABBB' #4
test_2 = 'AAABBBABAB' #4
test_case = [2,test_1,test_2]
print(alternatingCharacters(test_case))