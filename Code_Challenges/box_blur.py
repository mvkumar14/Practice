# Solved 072020
# CodeSignal
# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

a = [[1,1,1,2], 
 [1,7,1,2], 
 [1,1,1,2],
 [1,1,2,2]]

def box_blur(a):
    output = []
    print(len(a)-3)
    print(len(a[0])-3)
    for i in range(len(a)-2): # the height of the array:
        temp = []
        for j in range(len(a[0])-2): # the width of the array:
            r1 = sum(a[i][j:j+3])
            r2 = sum(a[i+1][j:j+3])
            r3 = sum(a[i+2][j:j+3])
            print(r1,r2,r3)
            temp.append((r1+r2+r3)//9)
        output.append(temp)
    print(output)
    return output

box_blur(a)

# One of the top solutions to this problem: 
def boxBlur(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans