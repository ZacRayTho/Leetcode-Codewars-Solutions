# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is 2.

def diagonalDifference(arr):
    left = 0
    right = 0
    for x in range(len(arr)):
        left += arr[x][x]
        right += arr[x][(len(arr) - 1) - x]
        print(left, right)

    
    return left - right if left-right > 0 else (left-right)*-1