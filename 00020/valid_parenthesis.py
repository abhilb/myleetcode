class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"[": "]", "{": "}", "(": ")"}
        for b in s:
            if b in "({[":
                stack.append(b)
            else:
                if stack:
                    last = stack.pop()
                    if match[last] != b:
                        return False
                else:
                    return False

        return len(stack) == 0


s = Solution()

# Input: s = "()"
# Output: true
assert s.isValid("()") == True

# Input: s = "()[]{}"
# Output: true
assert s.isValid("()[]{}") == True

# Input: s = "(]"
# Output: false
assert s.isValid("(]") == False

# Input: s = "([)]"
# Output: false
assert s.isValid("([)]") == False

# Input: s = "{[]}"
# Output: true
assert s.isValid("{[]}") == True

assert s.isValid("]") == False