"""
Trie
"""

from typing import List


class Solution2416:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """
        2416h Sum of Prefix Scores of Strings
        """
        class trie:
            def __init__(self):
                self.child = [None]*26
                self.score = 0

        t = trie()

        def insert(word: str):
            n = t
            for letter in word:
                c = n.child[ord(letter)-ord('a')]
                if not c:
                    c = trie()
                    n.child[ord(letter)-ord('a')] = c
                n = c
                n.score += 1

        def search(word: str) -> int:
            score = 0
            n = t
            for letter in word:
                c = n.child[ord(letter)-ord('a')]
                if not c:
                    return 0
                n = c
                score += n.score
            return score

        for word in words:
            insert(word)

        print(" ->", t.child)

        scores = []
        for word in words:
            scores.append(search(word))
        return scores


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
