import dijkstra as m


def test_Solution2577():
    # 2577h Minimum Time to Visit a Cell In a Grid
    assert m.Solution2577().minimumTime([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]) == 7
    print("---")
    assert m.Solution2577().minimumTime([[0, 2, 4], [3, 2, 1], [1, 0, 4]]) == -1
