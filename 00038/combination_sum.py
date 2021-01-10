from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.candidates = candidates
        self.target = target
        self.solve(target, [], 0)
        return self.result

    def solve(self, remain, seq, index: int) -> bool:
        if remain == 0:
            self.result.append(seq.copy())
            return
        for idx in range(index, len(self.candidates)):
            if remain - self.candidates[idx] >= 0:
                seq.append(self.candidates[idx])
                self.solve(remain - self.candidates[idx], seq, idx)
                seq.pop()


s = Solution()

print(s.combinationSum([2, 3, 6, 7], 7))
