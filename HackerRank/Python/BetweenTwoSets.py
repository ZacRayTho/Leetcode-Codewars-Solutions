
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
#

def getTotalX(a, b):
    # Write your code here
    mult = []
    for x in range(1, min(b) + 1):
        for y in a:
            if x % y != 0:
                break
            if y == a[len(a) - 1]:
                mult.append(x)
             
    print(mult)
    total = 0
    for x in mult:
        for y in b:
            print(x , y)
            print(y % x)
            if y % x != 0:
                break
            if y == b[len(b) - 1]:
                total += 1
                
    return total