from typing import List


class Solution2275:
    """
    2275m Largest Combination With Bitwise AND Greater Than Zero
    """
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 24

        mask = 1
        for i in range(24):
            print(mask)

            for n in candidates:
                if n & mask != 0:
                    count[i] += 1
            mask <<= 1

        return max(count)
