class Solution(object):
    def singleNumber(self, nums):
        freq = {}

        # Count frequency of each number
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Find the number that appears once
        for num in freq:
            if freq[num] == 1:
                return num
        