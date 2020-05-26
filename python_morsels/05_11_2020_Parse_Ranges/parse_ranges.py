# def parse_ranges(input_string):
#     temp = []
#     for i in  input_string.split(','):
#         temp.append(i.split('-'))
    
#     output = []
#     for i in temp:
#         output.extend(list(range(int(i[0]), int(i[1])+1)))
#     return output


def parse_ranges(input_string):
    temp = []
    for i in input_string.split(','):
        temp += i.split('-')
    
    pointer = 0
    start_range = pointer
    end_range = pointer + 1
    end = len(temp)
    while True:
        for i in range(int(temp[start_range]), int(temp[end_range])+1):
            yield i
        start_range += 2
        end_range += 2
        if start_range == end:
            break

# a = parse_ranges('1-2,4-4,8-10')
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
