# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
# This is a staircase of size n == 4:
   #
  ##
 ###
####
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

def staircase(n):
    for x in range(n):
        # print(x)
        for y in range(n):
            # print(y, "y", n, "n")
            if y + 1 >= n - x:
                print('#', end="")
            else:
                print(" ", end="")
        print("")