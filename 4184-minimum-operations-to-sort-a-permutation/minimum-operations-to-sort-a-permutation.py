from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        starts = []

        # Check rotations of sorted array
        k = nums[0]
        if all(nums[i] == (i + k) % n for i in range(n)):
            starts.append((0, k))

        # Check rotations of reversed sorted array
        k = (n - 1 - nums[0]) % n
        if all(nums[i] == (n - 1 - (i + k) % n)
               for i in range(n)):
            starts.append((1, k))

        if not starts:
            return -1

        # BFS
        q = deque()
        dist = {}

        for state in starts:
            if state not in dist:
                dist[state] = 0
                q.append(state)

        while q:
            orientation, k = q.popleft()
            d = dist[(orientation, k)]

            if orientation == 0 and k == 0:
                return d

            # Rotate left
            nxt = (orientation, (k + 1) % n)

            if nxt not in dist:
                dist[nxt] = d + 1
                q.append(nxt)

            # Reverse
            nxt = (1 - orientation, (-k) % n)

            if nxt not in dist:
                dist[nxt] = d + 1
                q.append(nxt)

        return -1