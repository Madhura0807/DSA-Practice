class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        min_distance = float('inf')
        first_index = -1
        last_index = -1
        prev_index = -1
        
        prev_node = head
        curr_node = head.next
        index = 2
        
        while curr_node.next:
            next_node = curr_node.next
            
            is_local_max = curr_node.val > prev_node.val and curr_node.val > next_node.val
            is_local_min = curr_node.val < prev_node.val and curr_node.val < next_node.val
            
            if is_local_max or is_local_min:
                if first_index == -1:
                    first_index = index
                else:
                    min_distance = min(min_distance, index - prev_index)
                prev_index = index
                last_index = index
                
            prev_node = curr_node
            curr_node = next_node
            index += 1
            
        if first_index == -1 or first_index == last_index:
            return [-1, -1]
            
        max_distance = last_index - first_index
        return [min_distance, max_distance]