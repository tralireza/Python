""" tests for Sorting module """

import sorting as m


def test_Solution539():
    assert m.Solution539().findMinDifference(["23:59", "00:00"]) == 1
    assert m.Solution539().findMinDifference(["00:00", "23:59", "00:00"]) == 0


def test_Solution3011():
    # 3011m Find if Array Can Be Sorted
    assert m.Solution3011().canSortArray([8, 4, 2, 30, 15]) is True
    assert m.Solution3011().canSortArray([1, 2, 3, 4, 5]) is True
    assert m.Solution3011().canSortArray([3, 16, 8, 4, 2]) is False
