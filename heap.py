import heapq
from typing import List


class Solution862:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        862h Shortest Subarray with Sum at Least K
        """
        nlen = len(nums)+1

        pq = []
        tsum = 0
        for i, n in enumerate(nums):
            tsum += n
            if tsum >= k:
                nlen = min(i+1, nlen)

            while pq and tsum - pq[0][0] >= k:
                nlen = min(i - heapq.heappop(pq)[1], nlen)

            heapq.heappush(pq, [tsum, i])

        return -1 if nlen > len(nums) else nlen


class Solution2406:
    def minGroup(self, intervals: List[List[int]]) -> int:
        """
        2406m Divide Intervals Into Minimum Number of Groups
        """
        intervals.sort()

        heap = []
        for interval in intervals:
            left, right = interval
            if heap and heap[0] < left:
                heapq.heappop(heap)
            heapq.heappush(heap, right)
            print(" ->", interval, " :: ", heap)

        return len(heap)
