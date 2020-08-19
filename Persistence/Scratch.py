# import Objects
# import Managers

# This is where I should run tests

def swap_adjacent_bits(n):
    print(bin(n)[2:])

even_mask = int('10101010',2)
odd_mask  = int('01010101',2)

test= int("01010100",2)

print(bin(test & (odd_mask>>1)))
print(bin(2**30))

print(bin(11^13), bin(-(11^13)), bin((11^13) & -(11 ^ 13)))