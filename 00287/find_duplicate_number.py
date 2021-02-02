from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            else:
                visited.add(num)


s = Solution()

assert s.findDuplicate2([1, 3, 4, 2, 2]) == 2
assert s.findDuplicate2([3, 1, 3, 4, 2]) == 3
assert s.findDuplicate2([1, 1]) == 1
assert s.findDuplicate2([1, 1, 2]) == 1
