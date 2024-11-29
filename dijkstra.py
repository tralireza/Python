from typing import List


class Solution2577:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        2577h Minimum Time to Visit a Cell In a Grid
        """
        import heapq

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        Rows, Cols = len(grid), len(grid[0])
        dirs = [1, 0, -1, 0, 1]

        visited = set()
        pq = [(grid[0][0], 0, 0)]
        while pq:
            print(" -> ", pq)

            time, r, c = heapq.heappop(pq)
            if (r, c) == (Rows-1, Cols-1):
                return time

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for i in range(4):
                x, y = r + dirs[i], c + dirs[i+1]
                if 0 <= x < Rows and 0 <= y < Cols and (x, y) not in visited:
                    wait = 0
                    if (grid[x][y] - time) & 1 == 0:
                        wait = 1

                    heapq.heappush(pq, (max(grid[x][y]+wait, time+1), x, y))

        return -1
