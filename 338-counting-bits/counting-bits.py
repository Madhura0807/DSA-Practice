class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize the DP array of size n + 1 with 0s
        ans = [0] * (n + 1)
        
        # Build the solution bottom-up from 1 to n
        for i in range(1, n + 1):
            # ans[i >> 1] gets the bits of the shifted number (i // 2)
            # (i & 1) checks if the last bit is 1 (odd number)
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans