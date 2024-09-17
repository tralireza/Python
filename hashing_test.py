import hashing as m


def test_Solution1371():
    """1371m Find the Longest Substring Containing Vowels in Even Counts"""
    assert m.Solution1371().findTheLongestSubstring("eleetminicoworoep") == 13
    assert m.Solution1371().findTheLongestSubstring("leetcodeisgreat") == 5
    assert m.Solution1371().findTheLongestSubstring("bcbcbc") == 6


def test_Solution884():
    """Uncommon Words from Two Sentences"""
    assert m.Solution884().uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
    assert m.Solution884().uncommonFromSentences("apple apple", "banana") == ["banana"]
