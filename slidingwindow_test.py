import slidingwindow as m


def test_Solution1652():
    # 1652 Defuse the Bomb

    assert m.Solution1652().decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
    assert m.Solution1652().decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
    assert m.Solution1652().decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]


def test_Solution2461():
    # 2461m Maximum Sum of Distinct Subarrays With Length K

    assert m.Solution2461().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15
    assert m.Solution2461().maximumSubarraySum([4, 4, 4], 3) == 0


def test_Solution2516():
    # 2516m Take K of Each Character From Left or Right

    assert m.Solution2516().takeCharacters("aabaaaacaabc", 2) == 8
    assert m.Solution2516().takeCharacters("a", 1) == -1
