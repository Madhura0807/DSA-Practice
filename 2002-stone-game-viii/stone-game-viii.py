class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Step 1: Compute prefix sums of the array
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + stones[i]
            
        # Step 2: Initialize the DP state from the end.
        # res keeps track of the maximum value of (prefix_sum[y] - dp[y]) 
        # as we iterate backwards from right to left.
        res = prefix_sum[-1]
        
        # Iterate backwards from index n-2 down to 1
        for i in range(n - 2, 0, -1):
            res = max(res, prefix_sum[i] - res)
            
        return res