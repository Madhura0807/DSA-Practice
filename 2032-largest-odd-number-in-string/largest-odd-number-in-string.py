class Solution:
    def largestOddNumber(self, s):
        # Remove leading zeros
        s = s.lstrip('0')

        # Find the last odd digit
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 1:
                return s[:i + 1]

        return ""