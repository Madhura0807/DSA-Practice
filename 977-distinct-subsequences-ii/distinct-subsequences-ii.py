class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        tot = 0
        dp = [0] * 26
        
        for c in s:
            idx = ord(c) - ord('a')
            new_subseqs = (tot + 1 - dp[idx]) % MOD
            tot = (tot + new_subseqs) % MOD
            dp[idx] = (dp[idx] + new_subseqs) % MOD
            
        return tot