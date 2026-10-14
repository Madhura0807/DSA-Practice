class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > 9 * num:
            return ""
        res = []
        for i in range(num):
            val = min(9, sum)
            res.append(str(val))
            sum -= val
        return "".join(res)