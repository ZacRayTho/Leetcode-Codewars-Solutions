# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

def birthdayCakeCandles(candles):
    total = 0
    tallest = 0
    for x in candles:
        if x > tallest:
            total = 1
            tallest = x
        elif x == tallest:
            total += 1

    return total
