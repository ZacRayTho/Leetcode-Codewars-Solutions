import math
# WORK INPROGRESS
def rgb(r, g, b):
# 100, 10, 1
# 16, 1

# divide number by 16
# rounded down the number that returns
#     print(math.floor(r / 16))
# get remainder of the division
#     print(r % 16)
    quotient = r
    final = ""
    while True:
        if quotient == 0:
            break
        final = final + str(quotient % 16)
        quotient = math.floor(quotient / 16)
    print(final)