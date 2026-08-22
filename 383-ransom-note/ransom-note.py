from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return not (st1 - st2)