class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = []
        for i in nums:
            new = i * i
            l.append(new)
        l=sorted(l)
        return l


        