from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for idx in range(1, len(prices)):
            profit = prices[idx] - prices[idx - 1]
            if profit > 0:
                result += profit
        return result


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
