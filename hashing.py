""" Hashing Solutions """

from typing import List


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


class Solution884:
    """Uncommon Words from Two Sentences"""

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter

        counter = Counter(s1.split(" ") + s2.split(" "))

        print(counter)

        return [w for w in counter if counter[w] == 1]
