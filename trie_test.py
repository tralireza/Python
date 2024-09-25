import trie as m


def test_Solution3043():
    # 3043m Find the Length of the Longest Common Prefix
    assert m.Solution3043().longestCommonPrefix([1, 10, 100], [1000]) == 3
    assert m.Solution3043().longestCommonPrefix([1, 2, 3], [4, 4, 4]) == 0
