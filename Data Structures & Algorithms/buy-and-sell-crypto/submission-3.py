class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0

        for right in range(1, len(prices)):
            while prices[right] < prices[left]:
                left += 1

            currProfit = prices[right] - prices[left]
            maxProfit = max(currProfit, maxProfit)
        
        return maxProfit

            