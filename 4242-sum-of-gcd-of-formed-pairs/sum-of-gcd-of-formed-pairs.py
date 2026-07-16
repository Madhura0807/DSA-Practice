from fractions import gcd

class Solution(object):
    def gcdSum(self, nums):
        mx = 0
        prefixGcd = []
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(x, mx))
        
        prefixGcd.sort()
        
        ans = 0
        left, right = 0, len(prefixGcd) - 1
        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return ans