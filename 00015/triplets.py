"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 

Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        if len(nums) >= 3:
            nums.sort()
            k = len(nums) - 1
            for i in range(len(nums)):
                j = i + 1
                while j < k:
                    tsum = nums[i] + nums[j] + nums[k]
                    if tsum == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
                        break
                    elif tsum < 0:
                        j += 1
                    else:
                        k -= 1
        return triplets


s = Solution()

assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert s.threeSum([]) == []
assert s.threeSum([0]) == []
assert s.threeSum([0, 0, 0, 0]) == [0, 0, 0], s.threeSum([0, 0, 0, 0])