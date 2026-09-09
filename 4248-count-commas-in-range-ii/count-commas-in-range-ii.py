class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        length = len(str(n))
        
        for digits in range(4, length + 1):
            start = 10 ** (digits - 1)
            end = 10 ** digits - 1 if digits < length else n
            
            commas = (digits - 1) // 3
            total += (end - start + 1) * commas
            
        return total