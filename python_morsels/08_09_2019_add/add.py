def add(matrix1,matrix2):
    count = 0
    tmp = []
    output = []
    for index, i in enumerate(matrix1):
        for index1,j in enumerate(i):
            int_sum = j + matrix2[index][index1]
            tmp.append(int_sum)
        output.append(tmp)
        tmp = []
    print(output)
    return output

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]

a = add(matrix1,matrix2)
