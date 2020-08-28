# Original Solution
def additionWithoutCarrying(param1, param2):
    smaller = min(param1,param2)
    larger = max(param1,param2)
    small_list = list(str(smaller))
    large_list = list(str(larger))
    output = []
    print(param1,param2)
    print(small_list,large_list)
    
    index_2= 0
    for index,i in enumerate(large_list):
        
        if index >= (len(large_list) - len(small_list)):
            print('index1:',index)
            print('index_two',index_2)
            print('larger_num',i)
            print('smaller_num',small_list[index_2])
            number = int(i)+int(small_list[index_2])
            if number > 9:
                digit = list(str(number))[-1]
                output.append(digit)
            else:
                output.append(str(number))
            index_2+=1
        else:
            print('index1:',index)
            print(i)
            output.append(i)
    return int("".join(output))

# Much cleaner solution (from reading the solutions)
# the reason that this works is because you stay in numeric space
# you are composing the number numerically not logically. 
# I was composing the number logically, and so I was working in 
# "string" space, and going back and forth. Here 
# you don't have to translate back and forth.
def additionWithoutCarrying(param1, param2):
    output = 0
    tenPower = 1
    while param1 or param2:
        output += tenPower * ((param1+param2)%10)
        param1 //= 10
        param2 //= 10
        tenPower *= 10
    return output