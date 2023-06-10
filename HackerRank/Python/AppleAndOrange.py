# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s - denotes start of house
#  2. INTEGER t - denotes end of house
#  3. INTEGER a - apple tree position
#  4. INTEGER b - orange tree position
#  5. INTEGER_ARRAY apples - array of positions of fallen apples from the tree
#  6. INTEGER_ARRAY oranges - array of positions of fallen oranges from the tree
# return 2 print lines of how many apples are in the house , and how many oranges are in the house

def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_app = 0
    house_ora = 0
    for apple in apples:
        if apple + a >= s and apple + a <= t:
            house_app += 1
    for orange in oranges: 
        if  orange + b >= s and orange + b <= t:
            house_ora += 1
    print(house_app)
    print(house_ora)
