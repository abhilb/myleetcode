from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        q = deque()
        for x in s:
            if x in q:
                while q:
                    if q.popleft() == x:
                        break

            q.append(x)
            maxlen = max(maxlen, len(q))
        return maxlen


s = Solution()

assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring(" ") == 1
assert s.lengthOfLongestSubstring("a") == 1
assert s.lengthOfLongestSubstring("dvdf") == 3