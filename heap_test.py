import heap as m


def test_Sloution2406():
    # 2406m Divide Intervals Into Minimum Number of Groups
    assert m.Solution2406().minGroup([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
    assert m.Solution2406().minGroup([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1
