
def alternatingSums(a):
    flag = True
    sum1 = 0
    sum2 = 0

    for i in a:
        if flag:
            sum1 += i
            flag = False
            print(sum1)
        else:
            sum2 += i
            flag = True
    
    print([sum1,sum2])
    return [sum1,sum2]

alternatingSums([50,60,60,45,70])