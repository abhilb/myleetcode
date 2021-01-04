from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        if nums:
            prev = nums[idx]
            for curr in nums:
                if curr == prev:
                    continue
                idx += 1
                nums[idx] = curr
                prev = curr
        return idx + 1, nums


s = Solution()

print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates([]))