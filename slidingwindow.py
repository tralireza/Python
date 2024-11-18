from typing import List


class Solution1652:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        1652 Defuse the Bomb
        """

        if k == 0:
            return [0] * len(code)

        start, end = 1, k
        if k < 0:
            start, end = len(code) + k, len(code)-1

        ksum = 0
        for i in range(start, end+1):
            ksum += code[i]

        rst = []
        for _ in range(len(code)):
            rst.append(ksum)

            end = (end+1) % len(code)
            ksum += code[end]
            ksum -= code[start]
            start = (start+1) % len(code)

        return rst
