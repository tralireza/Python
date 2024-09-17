""" tests for Sorting module """

import sorting as m


def test_Solution539():
    assert m.Solution539().findMinDifference(["23:59", "00:00"]) == 1
    assert m.Solution539().findMinDifference(["00:00", "23:59", "00:00"]) == 0
