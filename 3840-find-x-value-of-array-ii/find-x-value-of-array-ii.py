class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[node] = val
            self.tree_cnt[node][val] = 1
            return

        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self.build(nums, left_child, l, mid)
        self.build(nums, right_child, mid + 1, r)
        self._merge(node, left_child, right_child)

    def _merge(self, node: int, left: int, right: int):
        # Combined product modulo k
        self.tree_prod[node] = (self.tree_prod[left] * self.tree_prod[right]) % self.k

        # Combine prefix counts
        cnt = list(self.tree_cnt[left])
        left_prod = self.tree_prod[left]

        for r in range(self.k):
            if self.tree_cnt[right][r] > 0:
                rem = (left_prod * r) % self.k
                cnt[rem] += self.tree_cnt[right][r]

        self.tree_cnt[node] = cnt

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            v = val % self.k
            self.tree_prod[node] = v
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][v] = 1
            return

        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if idx <= mid:
            self.update(left_child, l, mid, idx, val)
        else:
            self.update(right_child, mid + 1, r, idx, val)

        self._merge(node, left_child, right_child)

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_cnt[node]

        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if qr <= mid:
            return self.query(left_child, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_child, mid + 1, r, ql, qr)

        left_prod, left_cnt = self.query(left_child, l, mid, ql, qr)
        right_prod, right_cnt = self.query(right_child, mid + 1, r, ql, qr)

        # Merge results from left and right children
        res_prod = (left_prod * right_prod) % self.k
        res_cnt = list(left_cnt)

        for rem in range(self.k):
            if right_cnt[rem] > 0:
                new_rem = (left_prod * rem) % self.k
                res_cnt[new_rem] += right_cnt[rem]

        return res_prod, res_cnt


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegmentTree(nums, k)
        ans = []
        n = len(nums)

        for idx, val, start, target_x in queries:
            st.update(0, 0, n - 1, idx, val)
            _, cnt = st.query(0, 0, n - 1, start, n - 1)
            ans.append(cnt[target_x])

        return ans