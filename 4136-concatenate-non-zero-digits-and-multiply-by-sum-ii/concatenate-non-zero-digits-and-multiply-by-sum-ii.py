class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        m = len(s)
        
        # 1. Filter out non-zero digits and track their original indices
        nz_digits = []
        for c in s:
            if c != '0':
                nz_digits.append(int(c))
        
        n = len(nz_digits)
        
        # 2. Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        # 3. Precompute prefix sums and prefix values for the non-zero digits
        pref_sum = [0] * (n + 1)
        pref_val = [0] * (n + 1)
        
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nz_digits[i]
            pref_val[i+1] = (pref_val[i] * 10 + nz_digits[i]) % MOD
            
        # 4. Create mapping from original string indices to nz_digits indices
        # next_nz[i] stores the index in nz_digits of the first non-zero char >= i
        next_nz = [n] * (m + 1)
        # prev_nz[i] stores the index in nz_digits of the last non-zero char <= i
        prev_nz = [-1] * (m + 1)
        
        curr = n
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                curr -= 1
            next_nz[i] = curr
            
        curr = -1
        for i in range(m):
            if s[i] != '0':
                curr += 1
            prev_nz[i] = curr

        # 5. Answer each query
        ans = []
        for l, r in queries:
            L = next_nz[l]
            R = prev_nz[r]
            
            # If there are no non-zero digits in the range
            if L > R:
                ans.append(0)
                continue
            
            # Extract the numerical value of nz_digits[L...R] % MOD
            length = R - L + 1
            x = (pref_val[R+1] - pref_val[L] * pow10[length]) % MOD
            
            # Extract the sum of digits in nz_digits[L...R]
            digit_sum = pref_sum[R+1] - pref_sum[L]
            
            # Calculate final answer for the query
            ans.append((x * digit_sum) % MOD)
            
        return ans