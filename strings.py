class Solution1813:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        1813m Sentence Similarity III
        """

        from collections import deque
        deque1, deque2 = deque(sentence1.split()), deque(sentence2.split())

        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.popleft()
            deque2.popleft()

        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop()
            deque2.pop()

        return not deque1 or not deque2


class Solution3163:
    def compressedString(self, word: str) -> str:
        """
        3163m String Compression III
        """

        compress = ""

        prv, count = word[0], 1
        for letter in word[1:]:
            if prv != letter or count == 9:
                compress += str(count) + prv
                prv, count = letter, 1
            else:
                count += 1

        compress += str(count) + prv
        return compress
