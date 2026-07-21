class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        initial_ones = s.count('1')
        t = '1' + s + '1'
        
        groups = []
        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            groups.append((t[i], j - i))
            i = j
            
        max_delta = 0
        
        for k in range(1, len(groups) - 1):
            char, _ = groups[k]
            if char == '1':
                prev_char, prev_len = groups[k - 1]
                next_char, next_len = groups[k + 1]
                
                if prev_char == '0' and next_char == '0':
                    max_delta = max(max_delta, prev_len + next_len)
                    
        return initial_ones + max_delta