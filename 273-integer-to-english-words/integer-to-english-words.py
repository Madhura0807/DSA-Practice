class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
            
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return []
            elif n < 20:
                return [ones[n]]
            elif n < 100:
                return [tens[n // 10]] + helper(n % 10)
            else:
                return [ones[n // 100], "Hundred"] + helper(n % 100)
        
        res = []
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                part = helper(num % 1000)
                if unit:
                    part.append(unit)
                res = part + res
            num //= 1000
            
        return " ".join(res).strip()