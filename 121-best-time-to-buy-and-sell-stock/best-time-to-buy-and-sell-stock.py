class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        max_profit = 0
        for right in range(len(prices)):
            if prices[left] >= prices[right]:
                left = right
            else:
                profit = abs(prices[left] - prices[right])
                right+=1
                max_profit = max(profit, max_profit)
        return max_profit


            
