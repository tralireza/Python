import dp as m


def test_Solution97():
    """97m Interleaving String"""

    assert m.Solution97().isInterleaving("", "", "") is True
    assert m.Solution97().isInterleaving("aabcc", "dbbca", "aadbbcbcac") is True
    assert m.Solution97().isInterleaving("aabcc", "dbbca", "aadbbbaccc") is False


def test_Solution139():
    """
    139m Word Break
    """
    assert m.Solution139().wordBreak("applepenapple", ["apple", "pen"]) is True
    assert m.Solution139().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_Solution198():
    """198m House Robber"""
    assert m.Solution198().rob([1, 2, 3, 1]) == 4
    assert m.Solution198().rob([2, 7, 9, 3, 1]) == 12


def test_Solution221():
    """221m Maximal Square"""
    assert (
        m.Solution221().maximalSquare(
            [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
        )
        == 4
    )
    assert m.Solution221().maximalSquare([["0", "1"], ["1", "0"]]) == 1
