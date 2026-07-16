import heapq

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
                
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next