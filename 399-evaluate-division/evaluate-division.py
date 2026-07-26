from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            
            queue = deque([(src, 1.0)])
            visited = {src}

            while queue:
                curr, product = queue.popleft()
                if curr == dst:
                    return product
                for neighbor, val in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * val))
            
            return -1.0

        return [bfs(q[0], q[1]) for q in queries]