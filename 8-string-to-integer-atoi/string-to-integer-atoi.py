class Solution:
    def myAtoi(self, s):
        i = 0
        num = 0
        sign = 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            num = num * 10 + int(s[i])
            i += 1
        num = num * sign
        if num > 2147483647:
            return 2147483647

        if num < -2147483648:
            return -2147483648

        return num