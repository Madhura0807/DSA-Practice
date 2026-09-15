class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            found = False
            for length in (k, k + 1):
                if i + length <= n:
                    sub = s[i : i + length]
                    if sub == sub[::-1]:
                        ans += 1
                        i += length
                        found = True
                        break
            if not found:
                i += 1
        return ans