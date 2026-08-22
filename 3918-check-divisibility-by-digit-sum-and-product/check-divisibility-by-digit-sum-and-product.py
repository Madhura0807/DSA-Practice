class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        for digit in str(n):
            d = int(digit)
            s += d
            p *= d
        return n % (s + p) == 0