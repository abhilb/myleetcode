from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        def generate(seq, target, mp):
            if mp < 0:
                return

            if mp == 0 and seq.count("(") == n and seq.count(")") == n:
                self.result.append(seq)
            else:
                if seq.count("(") <= target and seq.count(")") <= target:
                    generate(seq + "(", n, mp + 1)
                    generate(seq + ")", n, mp - 1)

        generate("(", n, 1)
        return self.result


s = Solution()

print(s.generateParenthesis(1))

# assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
# assert s.generateParenthesis(1) == ["()"]
