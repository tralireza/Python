import slidingwindow as m


def test_Solution1652():
    # 1652 Defuse the Bomb

    assert m.Solution1652().decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
    assert m.Solution1652().decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
    assert m.Solution1652().decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
