from typing import List


class Solution1652:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        1652 Defuse the Bomb
        """

        if k == 0:
            return [0] * len(code)

        start, end = 1, k
        if k < 0:
            start, end = len(code) + k, len(code) - 1

        ksum = 0
        for i in range(start, end+1):
            ksum += code[i]

        rst = []
        for _ in range(len(code)):
            rst.append(ksum)

            end = (end+1) % len(code)
            ksum += code[end]
            ksum -= code[start]
            start = (start+1) % len(code)

        return rst


class Solution2461:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        2461m Maximum Sum of Distinct Subarrays With Length K
        """

        xsum, ksum = 0, 0
        last = {}

        start = 0
        for end, n in enumerate(nums):
            ksum += n

            n_last = last.get(n, -1)
            while start <= n_last or end - start + 1 > k:
                ksum -= nums[start]
                start += 1
            last[n] = end

            if end - start + 1 == k:
                xsum = max(ksum, xsum)

        return xsum
