from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = 1500
        freq = [0] * (max_f + 1)
        for f, p in items:
            freq[f] += 1
            
        free_bonus = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                total = 0
                for mult in range(f, max_f + 1, f):
                    total += freq[mult]
                free_bonus[f] = total - 1
                
        dp = [0] * (budget + 1)
        
        for f, p in items:
            if p > budget:
                continue
            first_val = 1 + free_bonus[f]
            
            for b in range(budget, p - 1, -1):
                if dp[b - p] + first_val > dp[b]:
                    dp[b] = dp[b - p] + first_val
                    
            for b in range(p, budget + 1):
                if dp[b - p] + 1 > dp[b]:
                    dp[b] = dp[b - p] + 1
                    
        return max(dp)