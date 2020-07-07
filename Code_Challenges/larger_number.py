# Solved 07/07/2020
# Daily Interview Pro 
# e-mail

# Given a list of numbers, for each element find the next 
# element that is larger than the current element. 
# Return the answer as a list of indices. If there are no elements 
# larger than the current element, then use -1 instead.

def larger_number(nums):
    # Fill this in.
    # Pointer 1 tracks position
    # pointer 2 
    # maybe use a dictionary  for index:value?
    # maybe thats how python does it internally?

    # if you hit the end of the list and nothing 
    # is bigger
    # move pointer 1 up by 1
    # if you hit something bigger
    # that index = x
    # add n x's to the output array
    # where n = x-current index
    # move the pointer to x
    
    pointer = 0
    output = []
    flag = 0 
    while pointer < len(nums):
        current = nums[pointer]
        for index,i in enumerate(nums[pointer+1:]):
            if i > current:
                output.extend([pointer+index+1]*(index+1))
                flag = 1
                pointer += index + 1
                break
        if flag == 0:
            output.append(-1)
            pointer += 1
        flag = 0
    return output

  
# print [2, 2, 3, 4, -1, -1]
print(larger_number([3, 2, 5, 6, 9, 8]))
