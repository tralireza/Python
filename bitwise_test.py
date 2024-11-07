import bitwise as m


def test_Solution2275():
    # 2275m Largest Combination With Bitwise AND Greater Than Zero
    # 1 <= N <= 10^7
    assert m.Solution2275().largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4
    assert m.Solution2275().largestCombination([8, 8]) == 2
