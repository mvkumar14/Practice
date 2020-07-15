# 07152020
# NOT SOLVED YET


# Given a string with only ( and ), find the minimum number of characters 
# to add or subtract to fix the string such that the brackets are balanced.

# Questions:
# do you have to match them in isolated sets?
# can you have (()()) (actually maybe it doesn't matter it will always
# end up as a "matched set even if you try to "weave" them.)

# if you see ( then you have to add 1
# if you see a ) subtract one 

def fix_brackets(s):
    out_sum = 0
    open_sets = 0
    closed_sets = 0
    for char in s:
        if char == "(":
            out_sum += 1
            open_sets += 1
        else:
            out_sum -= 1
            if open_sets > 0:
                open_sets -= 1
    return abs(out_sum + open_sets)

print(fix_brackets('(()()) ))((('))
