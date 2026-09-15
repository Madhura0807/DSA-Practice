class Solution:

    def largestOverlap(
        self, img1: list[list[int]], img2: list[list[int]]
    ) -> int:
        n = len(img1)
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        count = {}
        max_overlap = 0

        for r1, c1 in pts1:
            for r2, c2 in pts2:
                shift = (r2 - r1, c2 - c1)
                count[shift] = count.get(shift, 0) + 1
                if count[shift] > max_overlap:
                    max_overlap = count[shift]

        return max_overlap