class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        valid_islands_count = 0
        
        def get_island_sum(r, c):
            stack = [(r, c)]
            visited[r][c] = True
            total_sum = 0
            
            while stack:
                curr_r, curr_c = stack.pop()
                total_sum += grid[curr_r][curr_c]
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_r, next_c = curr_r + dr, curr_c + dc
                    
                    if 0 <= next_r < rows and 0 <= next_c < cols:
                        if grid[next_r][next_c] > 0 and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            stack.append((next_r, next_c))
                            
            return total_sum

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and not visited[r][c]:
                    island_sum = get_island_sum(r, c)
                    if island_sum % k == 0:
                        valid_islands_count += 1
                        
        return valid_islands_count