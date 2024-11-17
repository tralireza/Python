import heap as m


def test_Solution862():
    # 862h Shortest Subarray with Sum at Least K
    assert m.Solution862().shortestSubarray([1], 1) == 1
    assert m.Solution862().shortestSubarray([1, 2], 4) == -1
    assert m.Solution862().shortestSubarray([2, -1, 2], 3) == 3


def test_Solution2406():
    # 2406m Divide Intervals Into Minimum Number of Groups
    assert m.Solution2406().minGroup([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
    assert m.Solution2406().minGroup([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1
