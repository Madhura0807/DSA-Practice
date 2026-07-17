from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
            
        total_pairs_divisible = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            c = 0
            for j in range(i, max_val + 1, i):
                c += count[j]
            total_pairs_divisible[i] = c * (c - 1) // 2
            
        gcd_count = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            exact_pairs = total_pairs_divisible[i]
            for j in range(2 * i, max_val + 1, i):
                exact_pairs -= gcd_count[j]
            gcd_count[i] = exact_pairs
            
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_count[i]
            
        ans = []
        for q in queries:
            idx = bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans