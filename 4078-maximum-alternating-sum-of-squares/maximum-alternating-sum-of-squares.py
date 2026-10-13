class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        A = sorted(x * x for x in nums)
        n = len(A)
        mid = n // 2
        return sum(A[mid:]) - sum(A[:mid])