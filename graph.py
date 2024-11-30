import collections

from typing import List


class Solution2097:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        """
        2097h Valid Arrangement of Pairs
        """

        adjm = collections.defaultdict(list)
        din, dout = collections.defaultdict(int), collections.defaultdict(int)

        for pair in pairs:
            v, u = pair[0], pair[1]
            adjm[v].append(u)
            dout[v] += 1
            din[u] += 1

        print("->", adjm)

        start = pairs[0][0]
        for v in dout:
            if dout[v] == din[v]+1:
                start = v

        path = []

        stack = [start]
        while stack:
            v = stack[-1]
            if adjm[v]:
                u = adjm[v].pop(0)
                stack.append(u)
            else:
                path.append(v)
                stack.pop()

        path.reverse()

        rst = []
        for i in range(1, len(path)):
            rst.append([path[i-1], path[i]])
        return rst
