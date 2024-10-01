import hashing as m


def test_Solution884():
    """Uncommon Words from Two Sentences"""
    assert m.Solution884().uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
    assert m.Solution884().uncommonFromSentences("apple apple", "banana") == ["banana"]


def test_Solution1371():
    """1371m Find the Longest Substring Containing Vowels in Even Counts"""
    assert m.Solution1371().findTheLongestSubstring("eleetminicoworoep") == 13
    assert m.Solution1371().findTheLongestSubstring("leetcodeisgreat") == 5
    assert m.Solution1371().findTheLongestSubstring("bcbcbc") == 6


def test_Solution1497():
    # Check If Array Pairs Are Divisible by k
    assert m.Solution1497().canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5) is True
    assert m.Solution1497().canArrange([1, 2, 3, 4, 5, 6], 7) is True
    assert m.Solution1497().canArrange([1, 2, 3, 4, 5, 6], 10) is False
