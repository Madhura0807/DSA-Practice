class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        from collections import Counter
        count = Counter(s)
        
        # We can use a backtracking function that returns the string if found
        def dfs(idx, path_counts):
            if idx == n:
                return ""
            
            target_char = target[idx]
            target_idx = ord(target_char) - ord('a')
            
            # 1. Try characters strictly greater than target_char first if we are already greater,
            # or try matching/exceeding.
            # To make it strictly greater, at some index i, we pick a char > target[idx] 
            # and then fill the rest with the smallest possible characters.
            
            # Let's check all characters from target_idx to 25
            for c_idx in range(target_idx, 26):
                char = chr(ord('a') + c_idx)
                if path_counts[char] > 0:
                    path_counts[char] -= 1
                    
                    # If this character is strictly greater than target[idx], 
                    # we can fill the rest of the string with the smallest available characters.
                    if c_idx > target_idx:
                        rem = []
                        for code in range(26):
                            ch = chr(ord('a') + code)
                            rem.append(ch * path_counts[ch])
                        return char + "".join(rem)
                    
                    # Otherwise, it's equal to target[idx], continue deeper
                    res = dfs(idx + 1, path_counts)
                    if res != "":
                        return char + res
                        
                    path_counts[char] += 1
            
            return ""

        return dfs(0, count)