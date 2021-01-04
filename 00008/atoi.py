"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.

Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned. """


class Solution:
    def convert(self, s: str) -> int:
        result = 0
        for idx in range(0, len(s)):
            if s[idx].isdigit():
                result = (result * 10) + int(s[idx])
            else:
                break
        return result

    def myAtoi(self, s: str) -> int:
        prev = None
        result = 0
        mult = 1
        s = s.strip()
        sign_map = {"-": -1}

        if len(s) > 0:
            start_idx = 1 if s[0] in "+-" else 0
            mult = sign_map.get(s[0], 1)

            result = mult * self.convert(s[start_idx:])
            if result < -(2 ** 31):
                result = -(2 ** 31)
            elif result > 2 ** 31 - 1:
                result = 2 ** 31 - 1

        return result


s = Solution()

assert s.myAtoi("3") == 3
assert s.myAtoi("3.14") == 3
assert s.myAtoi("42") == 42
assert s.myAtoi("   -42") == -42
assert s.myAtoi("4193 with words") == 4193
assert s.myAtoi("words and 987") == 0
assert s.myAtoi("-91283472332") == -2147483648
assert s.myAtoi("") == 0
assert s.myAtoi("+1") == 1
assert s.myAtoi("+-12") == 0
assert s.myAtoi("4294967296") == 2147483647
assert s.myAtoi("2147483648") == 2147483647
assert s.myAtoi("-5-") == -5
assert s.myAtoi("+") == 0