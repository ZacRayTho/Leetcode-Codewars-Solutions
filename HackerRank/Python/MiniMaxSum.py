# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
#  Then print the respective minimum and maximum values as a single line of two space-separated long integers.
def miniMaxSum(arr):
    # Write your code here
    max = 0
    min = sum(arr)
    for x in range(len(arr)):
        total = 0
        for y in range(len(arr)):
            if x != y:
                total += arr[y]
        if total > max:
            max = total
        if total < min:
            min = total

    print(min, max)
