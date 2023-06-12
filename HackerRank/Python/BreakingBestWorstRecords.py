# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

def breakingRecords(scores):
    min = 0
    max = 0
    minCount = 0
    maxCount = 0
    for score in scores:
        if min == 0 and max == 0 and score == scores[0]:
            min = score 
            max = score
        elif min > score:
            min = score
            minCount += 1
        elif max < score:
            max = score
            maxCount += 1
    return [maxCount, minCount]