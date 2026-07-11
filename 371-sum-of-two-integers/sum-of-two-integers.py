class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        
        # Force both a and b into 32-bit unsigned integer representations immediately
        a = a & mask
        b = b & mask
        
        while b:
            # Calculate the carry and mask it
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
            
        # If the 31st bit is set, it's a negative number in two's complement
        return a if a < 0x80000000 else ~(a ^ mask)