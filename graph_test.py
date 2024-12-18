import graph as m


def test_Solution2097():
    # 2097h Valid Arrangement of Pairs

    assert m.Solution2097().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]) == [[11, 9], [9, 4], [4, 5], [5, 1]]
    assert m.Solution2097().validArrangement([[1, 3], [3, 2], [2, 1]]) == [[1, 3], [3, 2], [2, 1]]
    assert m.Solution2097().validArrangement([[1, 2], [1, 3], [2, 1]]) == [[1, 2], [2, 1], [1, 3]]
