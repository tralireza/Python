import dp

def test_Solution97():
   assert dp.Solution97().isInterleaving("", "", "") == True
   assert dp.Solution97().isInterleaving("aabcc", "dbbca", "aadbbcbcac") == True 
   assert dp.Solution97().isInterleaving("aabcc", "dbbca", "aadbbbaccc") == False

# 221m Maximal Square
def test_solution221():
   assert dp.Solution221().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
   assert dp.Solution221().maximalSquare([["0","1"],["1","0"]]) == 1
