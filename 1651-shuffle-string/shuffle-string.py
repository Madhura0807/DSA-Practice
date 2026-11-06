class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [''] * len(s)
        for i, idx in enumerate(indices):
            res[idx] = s[i]
        return "".join(res)