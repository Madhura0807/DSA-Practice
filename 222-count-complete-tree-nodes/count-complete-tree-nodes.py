# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
            
        depth = 0
        node = root
        while node.left:
            depth += 1
            node = node.left
            
        if depth == 0:
            return 1
        low = 0
        high = (1 << depth) - 1
        
        def exists(idx, d, node):
            """
            Checks if the node at index 'idx' exists at the last level.
            Uses binary search to guide the path down from the root.
            """
            left, right = 0, (1 << d) - 1
            for _ in range(d):
                mid = left + (right - left) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        while low <= high:
            mid = low + (high - low) // 2
            if exists(mid, depth, root):
                low = mid + 1
            else:
                high = mid - 1
                
        return (1 << depth) - 1 + low