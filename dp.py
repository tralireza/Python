from typing import List

# 97m Interleaving String
class Solution97:
   def isInterleaving(self, s1: str, s2: str, s3: str) -> bool:
      R, C = len(s1), len(s2)
      if R + C != len(s3):
         return False
      if R == 0 or C == 0:
         return s1 == s3 or s2 == s3

      dp = [[False]*(C+1) for _ in range(R+1)]

      dp[0][0] = True
      for r in range(1, R+1):
         dp[r][0] = dp[r-1] and s1[r-1] == s3[r-1]
      for c in range(1, C+1):
         dp[0][c] = dp[0][c-1] and s2[c-1] == s3[c-1]

      for r in range(1, R+1):
         for c in range(1, C+1):
            dp[r][c] = dp[r-1][c] and s1[r-1] == s3[r+c-1] or dp[r][c-1] and s2[c-1] == s3[r+c-1]

      return dp[R][C]

# 221m Maximal Square
class Solution221:
   def maximalSquare(self, matrix: List[List[str]]) -> int:
      Rows, Cols = len(matrix), len(matrix[0])
      dp = [[0]*(Cols+1) for _ in range(Rows+1)]

      x = 0
      for r in range(Rows):
         for c in range(Cols):
            if matrix[r][c] == "1":
               dp[r+1][c+1] = 1 + min(dp[r][c], dp[r+1][c], dp[r][c+1])
               x = max(dp[r+1][c+1], x)

      print(dp)

      return x * x
