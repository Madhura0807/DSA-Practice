class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        visited = set()

        def dfs(r, c, k):
            if k < 0 or k > (m + n - 1) // 2:
                return False
            if r == m - 1 and c == n - 1:
                return k == 0
            
            state = (r, c, k)
            if state in visited:
                return False
            visited.add(state)

            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    delta = 1 if grid[nr][nc] == '(' else -1
                    if dfs(nr, nc, k + delta):
                        return True
            return False

        return dfs(0, 0, 1)