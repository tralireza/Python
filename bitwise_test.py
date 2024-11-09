import bitwise as m


def test_Solution2275():
    # 2275m Largest Combination With Bitwise AND Greater Than Zero
    # 1 <= N <= 10^7
    assert m.Solution2275().largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4
    assert m.Solution2275().largestCombination([8, 8]) == 2


def test_Solution3133():
    # 3133m Minimum Array End
    # 1 <= n, x <= 10^8

    def BR(n, x) -> int:
        r = x
        for _ in range(n-1):
            r = (r+1) | x

        print(" ->", r)
        return r

    assert BR(3, 4) == 6
    assert BR(2, 7) == 15
    assert BR(6715154, 7193485) == 55012476815

    print("TLE:")
    BR(69735293, 5563569)  # TLE
