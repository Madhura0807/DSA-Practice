class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        used_bits = 0
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # If the current number shares set bits with the existing window,
            # shrink the window from the left until the conflict is resolved.
            while used_bits & nums[right]:
                used_bits ^= nums[left]
                left += 1
            
            # Include nums[right] into the active window bitmask
            used_bits |= nums[right]
            
            # Update the max length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length