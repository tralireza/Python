import dp as m


def test_Solution97():
    """ 97m Interleaving String """
    assert m.Solution97().isInterleaving("", "", "") is True
    assert m.Solution97().isInterleaving("aabcc", "dbbca", "aadbbcbcac") is True
    assert m.Solution97().isInterleaving("aabcc", "dbbca", "aadbbbaccc") is False


def test_Solution139():
    """ 139m Word Break """
    assert m.Solution139().wordBreak("applepenapple", ["apple", "pen"]) is True
    assert m.Solution139().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_Solution198():
    """ 198m House Robber """
    assert m.Solution198().rob([1, 2, 3, 1]) == 4
    assert m.Solution198().rob([2, 7, 9, 3, 1]) == 12


def test_Solution221():
    """ 221m Maximal Square """
    assert m.Solution221().maximalSquare([["1", "0", "1", "0", "0"],
                                          ["1", "0", "1", "1", "1"],
                                          ["1", "1", "1", "1", "1"],
                                          ["1", "0", "0", "1", "0"]]) == 4
    assert m.Solution221().maximalSquare([["0", "1"], ["1", "0"]]) == 1


def test_Solution300():
    """ 300 Longest Increasing Subsequence """
    m.Solution300().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    m.Solution300().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4


def test_Solution322():
    """ 322m Coin Change """
    assert m.Solution322().coinChange([1, 2, 5], 11) == 3
    assert m.Solution322().coinChange([2], 3) == -1
    assert m.Solution322().coinChange([1], 0) == 0


def test_Solution646():
    """ 646m Maximum Length of Pair Chain """
    m.Solution646().findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2
    m.Solution646().findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3
