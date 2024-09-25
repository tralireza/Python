import trie as m


def test_Solution2416():
    # 2416h Sum of Prefix Scores of Strings
    assert m.Solution2416().sumPrefixScores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
    assert m.Solution2416().sumPrefixScores(["abcd"]) == [4]


def test_Solution3043():
    # 3043m Find the Length of the Longest Common Prefix
    assert m.Solution3043().longestCommonPrefix([1, 10, 100], [1000]) == 3
    assert m.Solution3043().longestCommonPrefix([1, 2, 3], [4, 4, 4]) == 0
