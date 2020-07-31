def digitDegree(n):
    if len(str(n)) == 1:
        return 0
    digit_degree = 0
    while True:
        digit_sum = 0
        digit_degree += 1
        for i in str(n):
            digit_sum += int(i)
        if digit_sum < 10:
            return digit_degree
        n = digit_sum
            