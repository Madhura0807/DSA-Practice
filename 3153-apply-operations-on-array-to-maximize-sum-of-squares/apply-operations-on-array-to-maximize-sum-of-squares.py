class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 30
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    bits[i] += 1
        
        arr = [0] * len(nums)
        for i in range(30):
            for j in range(bits[i]):
                arr[j] |= (1 << i)
                
        ans = 0
        for i in range(k):
            ans = (ans + arr[i] * arr[i]) % MOD
            
        return ans