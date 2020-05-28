def addBorder(picture):
    # find width
    # print width + 2 *s
    # prepend and append * to each line
    # print width + 2 *S
    
    width = len(picture[0])
    flrow = "*" * (width +2) #first and last row

    output = []
    output.append(flrow)

    for i in picture:
        row = "*" + i + "*"
        output.append(row)
    output.append(flrow)

    return output

print(addBorder(['abc','def']))