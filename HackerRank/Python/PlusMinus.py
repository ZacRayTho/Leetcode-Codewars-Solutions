# Print the ratios of positive, negative and zero values in the array. 
# Each value should be printed on a separate line with  digits after the decimal. 
# The function should not return a value.

def plusMinus(arr):
    # print to 6 decimal points
    # proportion of positive, negative, and zeros
    pos = 0
    neg = 0
    zer = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else: 
            zer += 1
    
    
    print(f"{pos/len(arr):.6f}")
    print(f"{neg/len(arr):.6f}")
    print(f"{zer/len(arr):.6f}")