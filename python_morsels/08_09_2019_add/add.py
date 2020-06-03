def add(*args):
    matrix1 = args[0]
    # check if the inputs are all the same size
    num_lists = len(args[0])
    len_list = len(args[0][0])
    for i in args:
        current_num_list = len(i)
        if num_lists != current_num_list:
            raise ValueError('Given matricies are not the same size')
        for j in i:
            current_len_list = len(j)
            if len_list != current_len_list:
                raise ValueError('Given matricies are not the same size')


    count = 0
    tmp = []
    output = []
    for index, i in enumerate(matrix1):
        for index1,j in enumerate(i):
            int_sum = 0
            for i in args:
                int_sum += i[index][index1]
            tmp.append(int_sum)
        output.append(tmp)
        tmp = []
    print(output)
    return output


def add2(matrix1,matrix2):
    """ Add corresponding numbers in 2D matrix """
    combined = []
    for row1,row2 in zip(matrix1,matrix2):
        tmp = [sum(column) for column in zip(row1,row2)]
        combined.append(tmp)
    
    return combined
    # Alternativley:
    # nest the list comprehension for a one line solution:
    # return [[sum(column) for column in zip(row1,row2)] for row1,row2 in zip(matrix1,matrix2)]

    # and allowing for any number of matricies:
    # return [[sum(column) for column in zip(*rows)] for rows in zip(*matricies)]

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
print(list(zip(matrix1,matrix2)))
a = add2(matrix1,matrix2)

def zipper(*args):
    return list(zip(*args))

# a = zipper(matrix1,matrix2,matrix1)
# b = zip(matrix1,matrix2,matrix1)
# print(list(b))
# print(a)


# interesting quirk of zip.
# when you put a star in front it treats
# the n items in the list as n inputs to the zip function (with m items each)
# without a star it treats the whole list as 1 input with n items
print('-'*30)
print(list(zip(matrix1)))
print(list(zip(*matrix1)))
