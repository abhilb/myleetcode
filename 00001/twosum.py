from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = [target - n for n in nums]
        for idx1, num in enumerate(nums):
            for idx2, diff in enumerate(diffs):
                if num == diff and idx1 != idx2:
                    return [idx1, idx2]
        raise RuntimeError()


s = Solution()

assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], target=6) == [1, 2]
assert s.twoSum([3, 3], target=6) == [0, 1]
