import bitwise as m


def test_Solution2275():
    # 2275m Largest Combination With Bitwise AND Greater Than Zero
    # 1 <= N <= 10^7
    assert m.Solution2275().largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4
    assert m.Solution2275().largestCombination([8, 8]) == 2


def test_Solution3097():
    # 3097m Shortest Subarray With OR at Least K II
    assert m.Solution3097().minimumSubarrayLength([1, 2, 3], 2) == 1
    assert m.Solution3097().minimumSubarrayLength([2, 1, 8], 10) == 3
    assert m.Solution3097().minimumSubarrayLength([1, 2], 0) == 1


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

    print("O(N) :: TLE:")
    assert BR(6715154, 7193485) == 55012476815  # TLE
    BR(69735293, 5563569)  # TLE

    print("O(logN):")
    assert m.Solution3133().minEnd(3, 4) == 6
    assert m.Solution3133().minEnd(2, 7) == 15
    assert m.Solution3133().minEnd(6715154, 7193485) == 55012476815
    assert m.Solution3133().minEnd(69735293, 5563569) == 142821814265
