""" Hashing Solutions """

from typing import List


class Solution884:
    """Uncommon Words from Two Sentences"""

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter

        counter = Counter(s1.split(" ") + s2.split(" "))

        print(counter)

        return [w for w in counter if counter[w] == 1]


class Solution1371:
    """Find the Longest Substring Containing Vowels in Even Counts"""

    def findTheLongestSubstring(self, s: str) -> int:
        lMask = [0] * 26
        lMask[ord("a") - ord("a")] = 16
        lMask[ord("e") - ord("a")] = 8
        lMask[ord("i") - ord("a")] = 4
        lMask[ord("o") - ord("a")] = 2
        lMask[ord("u") - ord("a")] = 1

        xSub = 0  # longest substring

        mMask = [-1] * 32
        mask = 0
        for i in range(len(s)):
            mask ^= lMask[ord(s[i]) - ord("a")]
            if mMask[mask] == -1 and mask > 0:
                mMask[mask] = i
            xSub = max(i - mMask[mask], xSub)
        return xSub


class Solution1497:
    """Check If Array Pairs Are Divisible by k"""

    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0]*k
        for n in arr:
            freq[(n % k + k) % k] += 1

        print(" ->", freq)

        if freq[0] & 1:
            return False
        for i in range(1, k//2+1):
            if freq[i] != freq[k-i]:
                return False

        return True


class Solution1590:
    """
    1590m Make Sum Divisible by P
    """

    def minSubarray(self, nums: List[int], p: int) -> int:
        tsum = sum(nums)
        t = tsum % p
        if t == 0:
            return 0

        mem = {0: -1}
        mlen = len(nums)

        csum = 0
        for i in range(len(nums)):
            csum = (csum + nums[i]) % p
            r = (csum - t + p) % p
            if r in mem:
                mlen = min(mlen, i - mem[r])
            mem[csum] = i

        print(mem)

        return -1 if mlen == len(nums) else mlen
