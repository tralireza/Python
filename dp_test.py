import dp

def test_Solution97():
   assert dp.Solution97().isInterleaving("", "", "") == True
   assert dp.Solution97().isInterleaving("aabcc", "dbbca", "aadbbcbcac") == True 
   assert dp.Solution97().isInterleaving("aabcc", "dbbca", "aadbbbaccc") == False
