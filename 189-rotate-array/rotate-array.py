class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        # Modify nums in-place
        nums[:] = nums[-k:] + nums[:-k]