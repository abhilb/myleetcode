class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        if x > -(2 ** 31) and x < (2 ** 31 - 1):
            x = abs(x)
            while x > 0:
                result = (result * 10) + (x % 10)
                x = x // 10

        if result > 2 ** 31 - 1 or result < -(2 ** 31):
            result = 0

        return result * sign


s = Solution()

assert s.reverse(123) == 321, s.reverse(123)
assert s.reverse(-123) == -321, s.reverse(-123)
assert s.reverse(120) == 21
assert s.reverse(0) == 0
assert s.reverse(1534236469) == 0, s.reverse(1534236469)