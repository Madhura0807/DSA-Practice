class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        memo = {}

        def get_target(r, c, d):
            state = (r, c, d)
            if state in memo:
                return memo[state]
            
            curr_r, curr_c, curr_d = r, c, d
            
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                if curr_d == 0:
                    curr_d = 1
                    curr_r += 1
                else:
                    curr_d = 0
                    curr_c += 1
            
            if not (0 <= curr_r < m and 0 <= curr_c < n):
                res = (-1, -1, -1)
            else:
                res = (curr_r, curr_c, curr_d)
                
            memo[state] = res
            return res

        dps = [0] * (m * n)
        
        curr_r, curr_c, curr_d = get_target(0, 1, 0)
        if curr_r != -1:
            dps[curr_r * n + curr_c] = (dps[curr_r * n + curr_c] + 1) % MOD
            
        curr_r, curr_c, curr_d = get_target(1, 0, 1)
        if curr_r != -1:
            dps[curr_r * n + curr_c] = (dps[curr_r * n + curr_c] + 1) % MOD
        
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if i == 0 and j == 0:
                    continue
                ways = dps[idx]
                if ways == 0:
                    continue
                
                r, c, d = get_target(i, j + 1, 0)
                if r != -1:
                    nidx = r * n + c
                    dps[nidx] = (dps[nidx] + ways) % MOD
                    
                r, c, d = get_target(i + 1, j, 1)
                if r != -1:
                    nidx = r * n + c
                    dps[nidx] = (dps[nidx] + ways) % MOD
                    
        return dps[(m - 1) * n + (n - 1)]