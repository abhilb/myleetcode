"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
"""

from typing import List
from collections import deque


class Solution:
    def maxArea(self, height: List[int]) -> int:
        begin = 0
        end = -1
        maxarea = 0
        count = len(height)
        while begin < count + end:
            maxarea = max(
                maxarea, min(height[begin], height[end]) * (count + end - begin)
            )
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1
        return maxarea


s = Solution()

assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

assert s.maxArea([1, 1]) == 1

assert s.maxArea([1, 2, 1]) == 2

assert s.maxArea([4, 3, 2, 1, 4]) == 16
