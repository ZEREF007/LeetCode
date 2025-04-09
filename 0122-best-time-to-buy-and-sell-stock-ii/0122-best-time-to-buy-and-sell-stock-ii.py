from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)): # 1 to length because we are goinna skip 1 cause 0 diesn't have previous index and we are trying to compare prices for prev day
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit