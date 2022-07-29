# O(n^2) time | O(1) space
def maxProfitBruteForce(prices):
    bestProfit = 0
    for buyDate in range(len(prices)):
        for sellDate in range(buyDate+1,len(prices)):
            profit = prices[sellDate] - prices[buyDate]
            if (profit > bestProfit):
                bestProfit = profit
    return bestProfit

# O(n) time | O(1) space
def maxProfitOptimized(prices):
    bestProfit = 0
    currentMin = prices[0]
    for i in range(1, len(prices)):
        if (prices[i] < currentMin):
            currentMin = prices[i]
            continue
        bestProfit = max(bestProfit, prices[i] - currentMin)
    return bestProfit

if __name__ == "__main__":
    prices = [7,1,5,4,6,4]
    print("max profit brute force:",maxProfitBruteForce(prices))
    print("max profit sliding window: ", maxProfitOptimized(prices))