class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        for length in range(l, r + 1):
            current_sum = sum(nums[:length])
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)
                
            for i in range(length, n):
                current_sum += nums[i] - nums[i - length]
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1