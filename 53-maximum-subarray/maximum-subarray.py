class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        csum = 0
        for num in nums:
            csum += num
            if csum > max_sum:
                max_sum = csum
            if csum < 0:
                csum = 0
        return max_sum
        