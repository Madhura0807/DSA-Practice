from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        litter_coords = []
        start_x, start_y = -1, -1
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_x, start_y = r, c
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))
                    
        num_litter = len(litter_coords)
        litter_map = {coord: i for i, coord in enumerate(litter_coords)}
        
        best_energy = {}
        queue = deque([(start_x, start_y, 0, energy, 0)])
        best_energy[(start_x, start_y, 0)] = energy
        
        target_mask = (1 << num_litter) - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, mask, e, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    next_energy = e - 1
                    if next_energy < 0:
                        continue
                        
                    next_mask = mask
                    if classroom[nx][ny] == 'L':
                        litter_idx = litter_map[(nx, ny)]
                        next_mask |= (1 << litter_idx)
                        
                    actual_energy = energy if classroom[nx][ny] == 'R' else next_energy
                    
                    state_key = (nx, ny, next_mask)
                    if state_key not in best_energy or actual_energy > best_energy[state_key]:
                        best_energy[state_key] = actual_energy
                        queue.append((nx, ny, next_mask, actual_energy, steps + 1))
                        
        return -1