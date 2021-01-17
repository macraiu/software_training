def numWaterBottles(numBottles, numExchange):
    howmany = numBottles
    while numBottles >= numExchange:
        remainder = numBottles % numExchange
        numBottles //= numExchange
        howmany += numBottles
        numBottles += remainder

    return howmany

print(numWaterBottles(2, 3))