import stack as m


def test_Solution962():
    # 962m Maximum Width Ramp

    assert m.Solution962().maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4
    assert m.Solution962().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
