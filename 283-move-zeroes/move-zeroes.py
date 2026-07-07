class Solution:
    def moveZeroes(self, nums):
        j = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Fill the remaining positions with zeros
        for i in range(j, len(nums)):
            nums[i] = 0