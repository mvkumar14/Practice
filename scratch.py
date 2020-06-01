import time
def factorial(num):
    return go(num,1)

def go(num,accumulator):
    if num == 1:
        return accumulator
    else:
        return go(num-1, num * accumulator)

start = time.time()
a = factorial(100)
print(a)
end = time.time()
print(end-start)

def factorial2(num):
    if num == 1:
        return 1
    else:
        return num * factorial2(num-1)

start = time.time()
a = factorial2(100)
print(a)
end = time.time()
print(end-start)