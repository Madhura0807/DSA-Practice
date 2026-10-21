class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0
        if len(s) == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        if s[0] == mn or s[-1] == mx:
            return 1
            
        has_mn_prefix = False
        for i in range(len(s) - 1):
            if s[i] == mn:
                has_mn_prefix = True
                break
                
        has_mx_suffix = False
        for i in range(1, len(s)):
            if s[i] == mx:
                has_mx_suffix = True
                break
                
        if not has_mn_prefix and not has_mx_suffix:
            return 3
            
        return 2