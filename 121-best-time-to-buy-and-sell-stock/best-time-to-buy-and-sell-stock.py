class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        prevDay, nextDay = 0,1
        while nextDay < len(prices):
            if prices[prevDay] < prices[nextDay]:
                profit = prices[nextDay] - prices[prevDay]
                maxProfit = max(maxProfit, profit)
            else:
                prevDay = nextDay
            nextDay +=1    
        return  maxProfit     