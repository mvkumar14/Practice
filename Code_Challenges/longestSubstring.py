# find the length of the longest non-repeating substring in a given string

# String input = 'aedfgaie' -> 'aedfg'

# is it the length of the substring, (a contiguous block of letters with no repeats)
# or just the number of unique characters? this seems like 


# iterate through the string
# while iterating if you see a new character then add 1 to counter
# counting length
# return counter

# def numUnique()

def longestSubstring(inputString):
    temp = []
    max_str = []
    for index,i in enumerate(inputString):
        for j in inputString[index:]:
            if j in temp:
                if len(temp) > len(max_str):
                    max_str = temp
                temp = []
                break
            else:
                temp.append(j)
    return len(max_str), ''.join(max_str)
# we can optimize this further by making a dictionaryu
# that keeps track of the position of the letters
# and movese the left pointer up to the position past the repeated letter
# ex: in sequence agqifcfdska the first longest substring goes to the second f
# at that point every substring till the c will be smaller than the first substring
# cause it will hit the same f roadbloak. So move the pointer up to c and start
# checking from there


# I'm playing with dictionaries here and comparing to above
def longestSubstring2(inputString):
    temp_dict = {}
    counter = 1
    for index, i in enumerate(inputString):
        if temp_dict.__contains__(i):
            print("This is attempt number:", counter)
            print(temp_dict,len(temp_dict))
            counter += 1
            temp_dict = {}
        else:
            temp_dict[i] = [index]
    print("This is attempt number:", counter)
    print(temp_dict,len(temp_dict))
    return temp_dict


my_str = 'adkoalsoblawbjas'
print(longestSubstring2(my_str))
print(longestSubstring(my_str))