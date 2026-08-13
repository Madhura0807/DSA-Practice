class Node:
    def __init__(self, char=""):
        self.mx = 1 if char else 0
        self.pref = 1 if char else 0
        self.suff = 1 if char else 0
        self.lc = char
        self.rc = char

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self._build(s, 0, 0, self.n - 1)

    def _merge(self, left: Node, right: Node, l_len: int, r_len: int) -> Node:
        res = Node()
        res.lc = left.lc
        res.rc = right.rc

        res.pref = left.pref
        if left.pref == l_len and left.rc == right.lc:
            res.pref += right.pref

        res.suff = right.suff
        if right.suff == r_len and right.lc == left.rc:
            res.suff += left.suff

        res.mx = max(left.mx, right.mx)
        if left.rc == right.lc:
            res.mx = max(res.mx, left.suff + right.pref)

        return res

    def _build(self, s: str, node: int, l: int, r: int):
        if l == r:
            self.tree[node] = Node(s[l])
            return
        mid = (l + r) // 2
        self._build(s, 2 * node + 1, l, mid)
        self._build(s, 2 * node + 2, mid + 1, r)
        self.tree[node] = self._merge(
            self.tree[2 * node + 1],
            self.tree[2 * node + 2],
            mid - l + 1,
            r - mid
        )

    def update(self, node: int, l: int, r: int, idx: int, ch: str):
        if l == r:
            self.tree[node] = Node(ch)
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node + 1, l, mid, idx, ch)
        else:
            self.update(2 * node + 2, mid + 1, r, idx, ch)
        self.tree[node] = self._merge(
            self.tree[2 * node + 1],
            self.tree[2 * node + 2],
            mid - l + 1,
            r - mid
        )


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        ans = []
        n = len(s)

        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(0, 0, n - 1, idx, ch)
            ans.append(st.tree[0].mx)

        return ans