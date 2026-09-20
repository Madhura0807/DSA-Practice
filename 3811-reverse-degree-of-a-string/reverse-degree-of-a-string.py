class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            reversed_alpha_pos = 26 - (ord(char) - ord('a'))
            total += reversed_alpha_pos * i
        return total