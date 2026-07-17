class Solution:
    def removeOuterParentheses(self, s):
        result = ""
        count = 0

        for ch in s:
            if ch == '(':
                if count > 0:
                    result += ch
                count += 1
            else:
                if count > 1:
                    result += ch
                count -= 1

        return result