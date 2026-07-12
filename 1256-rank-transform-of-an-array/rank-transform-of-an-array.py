class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_unique = sorted(list(set(arr)))
        
        rank_map = {}
        for rank, num in enumerate(sorted_unique, 1):
            rank_map[num] = rank
        
        return [rank_map[num] for num in arr]