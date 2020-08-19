from collections import Counter

def digitsProduct(product):
    # if its prime then the answer is -1
    # else find the factors, and then 
    # sort them and join them
    if product == 0 :
        return 10
    elif product == 1:
        return 1
    elif product < 10:
        return int("1"+str(product))
    
    factors = find_factors(product) 
    if factors == product:
        return -1

    num = sorted(reduce_list(factors))
    print(num)
    
    if num[-1] > 9:
        return -1

    return int("".join([str(i) for i in num]))

def find_factors(number):
    factors_list = []
    for i in list(range(2,number))[::-1]:
        if number % i == 0:
            a = find_factors(i)
            b = find_factors(number//i)
            try:
                factors_list.extend(a)
            except TypeError:
                factors_list.append(a)
            try:
                factors_list.extend(b)
            except TypeError:
                factors_list.append(b)
            break
    # print(factors_list)
    if len(factors_list) == 0:
        return number # prime number so no factors
    else:
        return factors_list

def reduce_list(factors):
    # reduce a list of factors to a 
    # smaller list of one digit factors
    # this means if there are combos 
    # of 4,2  3,3  3,2  or 2,2
    # turn them into their multiples
    if len(factors) == 1:
        return factors
    frequency = Counter(factors)
    # print(dict(frequency))
    while frequency[3] >= 2:
        factors.remove(3)
        factors.remove(3)
        factors.append(9)
        frequency[3] -= 2
    while frequency[3] and frequency[2]:
        factors.remove(3)
        factors.remove(2)
        factors.append(6)
        frequency[3] -= 1
        frequency[2] -= 1
    while frequency[2] >= 3:
        factors.remove(2)
        factors.remove(2)
        factors.remove(2)
        factors.append(8)
        frequency[2] -= 3
    while frequency[2] >= 2:
        factors.remove(2)
        factors.remove(2)
        factors.append(4)
        frequency[2] -= 2
    return factors


for i in range(200):
    print( "number:",i )
    print(digitsProduct(i))
