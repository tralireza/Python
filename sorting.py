""" Sorting Solutions """

from typing import List


class Solution539:
    """
    539m Minimum Time Difference
    """

    def findMinDifference(self, timePoints: List[str]) -> int:
        Ms = [60 * int(t[:2]) + int(t[3:]) for t in timePoints]
        Ms.sort()

        print(Ms)

        r = 720
        for i in range(len(Ms) - 1):
            r = min(Ms[i + 1] - Ms[i], r)
        return min(1440 - (Ms[-1] - Ms[0]), r)


class Solution3011:
    """
    3011m Find if Array Can Be Sorted
    """

    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)

        # BubbleSort
        for i in range(N):
            for j in range(N - i - 1):
                if nums[j] > nums[j+1]:
                    if bin(nums[j]).count("1") == bin(nums[j+1]).count("1"):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False

        return True
