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


class Solution3097:
    """
    3097m Shortest Subarray With OR at Least K ||
    """

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        nlen = len(nums) + 1

        special = [0] * 32

        left, value = 0, 0
        for right in range(len(nums)):
            for i in range(32):
                if nums[right] & (1 << i):
                    special[i] += 1
                    if special[i] == 1:
                        value += 1 << i

            while left <= right and value >= k:
                nlen = min(right - left + 1, nlen)
                for i in range(32):
                    if nums[left] & (1 << i):
                        special[i] -= 1
                        if special[i] == 0:
                            value -= 1 << 1
                left += 1

        if nlen > len(nums):
            return -1
        return nlen


class Solution3133:
    """
    3133m Minimum Array End
    """

    def minEnd(self, n: int, x: int) -> int:
        r = x

        mask = 1
        n -= 1
        while n > 0:
            if (x & mask) == 0:
                r |= (n & 1) * mask
                n >>= 1
            mask <<= 1

        print(" ->", r)
        return r
