import heapq

class Solution(object):
    def maximumScore(self, nums, s):
        max_heap = []
        total_score = 0
        
        for i in range(len(s)):
            heapq.heappush(max_heap, -nums[i])
            if s[i] == '1':
                total_score += -heapq.heappop(max_heap)
                
        return total_score