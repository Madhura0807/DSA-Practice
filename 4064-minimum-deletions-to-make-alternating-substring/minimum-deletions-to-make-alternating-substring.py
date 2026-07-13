class Solution(object):
    def minDeletions(self, s, queries):
        n = len(s)
        s_list = list(s)
        bit = [0] * (n + 1)
        
        def update(idx, val):
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res
            
        def get_val(i):
            if i <= 0 or i >= n:
                return 0
            return 1 if s_list[i] == s_list[i-1] else 0

        for i in range(1, n):
            if s_list[i] == s_list[i-1]:
                update(i, 1)
                
        ans = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                
                prev_j = get_val(j)
                prev_next = get_val(j + 1)
                
                s_list[j] = 'B' if s_list[j] == 'A' else 'A'
                
                new_j = get_val(j)
                new_next = get_val(j + 1)
                
                if new_j != prev_j:
                    update(j, new_j - prev_j)
                if new_next != prev_next:
                    update(j + 1, new_next - prev_next)
            else:
                l, r = q[1], q[2]
                if l == r:
                    ans.append(0)
                else:
                    ans.append(query(r) - query(l))
                    
        return ans