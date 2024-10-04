import hashing as m


def test_Solution884():
    # Uncommon Words from Two Sentences
    assert m.Solution884().uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
    assert m.Solution884().uncommonFromSentences("apple apple", "banana") == ["banana"]


def test_Solution1371():
    # 1371m Find the Longest Substring Containing Vowels in Even Counts
    assert m.Solution1371().findTheLongestSubstring("eleetminicoworoep") == 13
    assert m.Solution1371().findTheLongestSubstring("leetcodeisgreat") == 5
    assert m.Solution1371().findTheLongestSubstring("bcbcbc") == 6


def test_Solution1497():
    # Check If Array Pairs Are Divisible by k
    assert m.Solution1497().canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5) is True
    assert m.Solution1497().canArrange([1, 2, 3, 4, 5, 6], 7) is True
    assert m.Solution1497().canArrange([1, 2, 3, 4, 5, 6], 10) is False


def test_Solution1590():
    # 1590m Make Sum Divisible by P
    assert m.Solution1590().minSubarray([3, 1, 4, 2], 6) == 1
    assert m.Solution1590().minSubarray([6, 3, 5, 2], 9) == 2
    assert m.Solution1590().minSubarray([1, 2, 3], 6) == 0


def test_Solution2491():
    # 2491m Divide Player Into Teams of Equal Skill
    assert m.Solution2491().dividePlayers([3, 2, 5, 1, 3, 4]) == 22
    assert m.Solution2491().dividePlayers([3, 4]) == 12
    assert m.Solution2491().dividePlayers([1, 1, 2, 3]) == -1
