class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = {(0, 0): 1}
        
        for num in nums:
            next_dp = {}
            for (g1, g2), count in dp.items():
                next_dp[(g1, g2)] = (next_dp.get((g1, g2), 0) + count) % MOD
                
                ng1 = num if g1 == 0 else gcd(g1, num)
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                ng2 = num if g2 == 0 else gcd(g2, num)
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + count) % MOD
                
        return ans