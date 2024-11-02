"""
Dynamic Programming Solutions
"""

from typing import List


class Solution97:
    """
    97m Interleaving String
    """

    def isInterleaving(self, s1: str, s2: str, s3: str) -> bool:
        R, C = len(s1), len(s2)
        if R + C != len(s3):
            return False
        if R == 0 or C == 0:
            return s1 == s3 or s2 == s3

        dp = [[False] * (C+1) for _ in range(R+1)]

        dp[0][0] = True
        for r in range(1, R+1):
            dp[r][0] = dp[r-1][0] and s1[r-1] == s3[r-1]
        for c in range(1, C+1):
            dp[0][c] = dp[0][c-1] and s2[c-1] == s3[c-1]

        for r in range(1, R+1):
            for c in range(1, C+1):
                dp[r][c] = dp[r-1][c] and s1[r-1] == s3[r+c-1] or dp[r][c-1] and s2[c-1] == s3[r+c-1]

        return dp[R][C]


class Solution139:
    """
    139m Word Break
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        segment = [False] * (len(s) + 1)
        segment[0] = True

        for ls in range(1, len(s) + 1):
            for w in words:
                lw = len(w)
                if ls - lw >= 0 and segment[ls - lw] and s[ls - lw:ls] == w:
                    segment[ls] = True

        return segment[-1]


class Solution198:
    """
    198m House Robber
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cash = [0] * len(nums)
        cash[0], cash[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cash[i] = max(cash[i - 2] + nums[i], cash[i - 1])

        print(nums, " -> ", cash)

        return cash[-1]


class Solution221:
    """
    221m Maximal Square
    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        Rows, Cols = len(matrix), len(matrix[0])
        dp = [[0] * (Cols + 1) for _ in range(Rows + 1)]

        x = 0
        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == "1":
                    dp[r + 1][c + 1] = 1 + min(dp[r][c], dp[r + 1][c], dp[r][c + 1])
                    x = max(dp[r + 1][c + 1], x)

        print(dp)

        return x * x


class Solution300:
    """
    300m Longest Increasing Subsequence
    """

    def lengthOfLIS(slef, nums: List[int]) -> int:
        lis = [1] * len(nums)
        for right in range(1, len(lis)):
            for left in range(0, right):
                if nums[right] > nums[left]:
                    lis[right] = max(lis[left]+1, lis[right])

        print(lis)

        return max(lis)


class Solution322:
    """
    322m Coin Change
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        change = [INF] * (amount+1)
        change[0] = 0
        for c in coins:
            if c <= amount:
                change[c] = 1

        for t in range(1, amount+1):
            for c in coins:
                if t >= c:
                    change[t] = min(change[t], change[t-c] + 1)

        print(f'{amount}? {coins} -> {change}')

        return change[amount] if change[amount] != INF else -1


class Solution646:
    """
    646m Maximum Length of Pair Chain
    """

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda lst: lst[1])

        lchain = [1] * len(pairs)
        for right in range(1, len(pairs)):
            for left in range(0, right):
                if pairs[right][0] > pairs[left][1]:
                    lchain[right] = max(lchain[left]+1, lchain[right])

        print(pairs, " -> ", lchain)

        return max(lchain)


class Solution2463:
    """
    2463h Minimum Total Distance Traveled
    """

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])

        fixes = []
        for f in factory:
            for _ in range(f[1]):
                fixes.append(f[0])

        print(fixes)

        R, F = len(robot), len(fixes)
        dp = [[0] * (F+1) for _ in range(R+1)]

        for r in range(R):
            dp[r][F] = 1e12

        for r in range(R-1, -1, -1):
            for f in range(F-1, -1, -1):
                assign = abs(robot[r]-fixes[f]) + dp[r+1][f+1]
                skip = dp[r][f+1]

                dp[r][f] = min(assign, skip)

        return dp[0][0]


class Solution2707:
    """
    2707m Extra Characters in a String
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        extra = [0]*(len(s)+1)

        for start in range(len(s)-1, -1, -1):
            extra[start] = 1 + extra[start+1]
            for end in range(start+1, len(s)+1):
                if s[start:end] in dictionary:
                    extra[start] = min(extra[start], extra[end])

        print(" ->", extra)

        return extra[0]
