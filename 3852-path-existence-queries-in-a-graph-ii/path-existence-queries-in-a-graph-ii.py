class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Create pairs of (value, original_index) and sort them
        sorted_nodes = sorted((nums[i], i) for i in range(n))
        
        # parent[i] will store the index of the node with the largest value <= nums[i] + maxDiff
        parent = list(range(n))
        
        # Use two pointers / binary search to find the greedy next step for each node
        right = 0
        for i in range(n):
            val, idx = sorted_nodes[i]
            # Move the right pointer to the largest value within maxDiff
            while right + 1 < n and sorted_nodes[right + 1][0] <= val + maxDiff:
                right += 1
            # The best target node is the one at the 'right' pointer
            parent[idx] = sorted_nodes[right][1]
            
        # Set up binary lifting table
        # LOG = 17 is sufficient since 2^17 > 10^5
        LOG = 17
        up = [[i] * n for _ in range(LOG)]
        up[0] = parent
        
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k-1][up[k-1][i]]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            # Ensure nums[u] <= nums[v] to always move in the positive direction
            if nums[u] > nums[v]:
                u, v = v, u
                
            # If they are already directly connected
            if nums[v] - nums[u] <= maxDiff:
                ans.append(1)
                continue
                
            # We want to find the number of steps to reach a value >= target_val
            target_val = nums[v] - maxDiff
            steps = 0
            curr = u
            
            # Lift curr as high as possible while its value is strictly less than target_val
            for k in range(LOG - 1, -1, -1):
                nxt = up[k][curr]
                if nums[nxt] < target_val:
                    curr = nxt
                    steps += (1 << k)
                    
            # After lifting, check if the immediate next greedy jump reaches or exceeds target_val
            nxt = up[0][curr]
            if nums[nxt] >= target_val and nums[nxt] > nums[curr]:
                # 1 step to reach nxt, and 1 final step from nxt to v
                ans.append(steps + 2)
            else:
                ans.append(-1)
                
        return ans