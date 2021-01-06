from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = defaultdict(list)
        zag = True
        idx = 0
        for x in s:
            rows[idx].append(x)

            if idx == 0 or idx == numRows - 1:
                zag = not zag
            idx += -1 if zag else 1

        result = ""
        for x in rows.values():
            result += "".join(x)
        return result


s = Solution()

print(s.convert(s="PAYPALISHIRING", numRows=3))
