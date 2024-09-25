"""
Trie
"""

from typing import List


class Solution3043:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        3043m Find the Length of the Longest Common Prefix
        """
        trie = set()
        for n in arr1:
            while n > 0:
                trie.add(n)
                n //= 10

        print(" ->", trie)

        longest = 0
        for n in arr2:
            while n not in trie and n > 0:
                n //= 10
            if n > 0:
                ln = 0
                while n > 0:
                    ln += 1
                    n //= 10
                longest = max(ln, longest)

        return longest
