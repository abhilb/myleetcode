from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


s = Solution()
print(s.singleNumber([2, 2, 3, 2]))
print(s.singleNumber([4, 4, 7, 4]))
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(s.singleNumber([2, 1, 2, 1, 2, 1, 80]))
