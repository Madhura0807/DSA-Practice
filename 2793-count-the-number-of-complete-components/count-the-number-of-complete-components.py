class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
       
        for i in range(n):
            if not visited[i]:
                component_nodes = []
                
            
                stack = [i]
                visited[i] = True
                
                while stack:
                    curr = stack.pop()
                    component_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
            
                V = len(component_nodes)
                is_complete = True
                
                for node in component_nodes:
                    if len(adj[node]) != V - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    complete_components += 1
                    
        return complete_components