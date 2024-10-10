from typing import List


class Solution962:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        962m Maximum Width Ramp
        """

        indices = [x for x in range(len(nums))]
        indices.sort(key=lambda x: (nums[x], x))

        print(nums, "=>", indices)

        xwidth = 0
        i = len(nums)
        for j in indices:
            xwidth = max(j - i, xwidth)
            i = min(j, i)

        return xwidth
