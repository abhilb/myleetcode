from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = prices[0]
        for idx in range(len(prices)):
            profit = prices[idx] - minprice
            if prices[idx] < minprice:
                minprice = prices[idx]
            elif profit > maxprofit:
                maxprofit = profit
        return maxprofit


s = Solution()

print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
