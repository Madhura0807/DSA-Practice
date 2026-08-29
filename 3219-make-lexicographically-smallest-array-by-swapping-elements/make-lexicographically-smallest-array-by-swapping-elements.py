class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each number with its original index
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        ans = [0] * n
        
        # Groups will store lists of (val, index) that belong to the same component
        groups = []
        current_group = []
        
        for val, idx in indexed_nums:
            if not current_group or val - current_group[-1][0] <= limit:
                current_group.append((val, idx))
            else:
                groups.append(current_group)
                current_group = [(val, idx)]
        if current_group:
            groups.append(current_group)
            
        # For each group, sort the indices and assign the sorted values back
        for group in groups:
            values = sorted([val for val, idx in group])
            indices = sorted([idx for val, idx in group])
            
            for i, idx in enumerate(indices):
                ans[idx] = values[i]
                
        return ans