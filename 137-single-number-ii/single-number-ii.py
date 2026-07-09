class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        # Iterate through every bit position (0 to 31 for 32-bit integers)
        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Extract the i-th bit of the number
                if (num >> i) & 1:
                    bit_sum += 1
            
            # If the bit sum is not divisible by 3, the single number has a 1 here
            if bit_sum % 3 != 0:
                # Handle Python's infinite precision integers for negative numbers
                if i == 31: 
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans