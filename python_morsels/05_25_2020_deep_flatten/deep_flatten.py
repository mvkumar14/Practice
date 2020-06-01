def deep_flatten(in_list):
    out_list = []
    for i in in_list:
        if type(i) == str:
            out_list.append(i)
        elif hasattr(i,'__iter__'):
            out_list.extend(deep_flatten(i))
        else:
            out_list.append(i)
    return out_list


a = [(1,2),3,4,5,[4,4,5,6]]
a = [['cats', ['carl', 'cate']],['dogs', ['darlene', 'doug']]]

b = deep_flatten(a)
print(b)