from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map row -> bitmask of reserved seats (seats 2 to 9)
        rows = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] |= (1 << (seat - 2))
        
        # Unreserved rows can hold 2 groups each
        ans = (n - len(rows)) * 2
        
        # Masks for checking availability:
        # Left: seats 2,3,4,5 -> bits 0,1,2,3 -> 0b00001111 (15)
        # Right: seats 6,7,8,9 -> bits 4,5,6,7 -> 0b11110000 (240)
        # Middle: seats 4,5,6,7 -> bits 2,3,4,5 -> 0b00111100 (60)
        left_mask = 0b00001111
        right_mask = 0b11110000
        middle_mask = 0b00111100
        
        for mask in rows.values():
            left_open = (mask & left_mask) == 0
            right_open = (mask & right_mask) == 0
            
            if left_open and right_open:
                ans += 2
            elif left_open or right_open or ((mask & middle_mask) == 0):
                ans += 1
                
        return ans