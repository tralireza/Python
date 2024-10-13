import heapq
from typing import List


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
            print(" ->", heap)

        return len(heap)
