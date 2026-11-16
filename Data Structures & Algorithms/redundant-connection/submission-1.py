class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_set = [set() for _ in range(n+1)]
        degree = [0 for _ in range(n+1)]

        for edge in edges:
            a, b = edge
            adj_set[a].add(b)
            adj_set[b].add(a)

            degree[a] += 1
            degree[b] += 1

        one_degrees = deque()
        for i, d in enumerate(degree):
            if d == 1:
                one_degrees.appendleft(i)
        
        while one_degrees:
            node = one_degrees.pop()
            print(node)
            for nei in adj_set[node]:
                adj_set[nei].remove(node)
                degree[nei] -= 1
                degree[node] = 0
                
                if degree[nei] == 1:
                    one_degrees.appendleft(nei)

        start_node = -1
        for i, d in enumerate(degree):
            if d > 0:
                start_node = i
                break
        
        current_node = start_node
        prev = -1
        valid_edges = set()
        while True:
            print(current_node)
            for nei in adj_set[current_node]:
                if nei != prev:
                    valid_edges.add((nei, current_node))
                    prev = current_node
                    current_node = nei
                    break
            if current_node == start_node:
                break
        
        print(valid_edges)

        for edge in edges[::-1]:
            a, b = edge
            if (a, b) in valid_edges or (b, a) in valid_edges:
                return edge
        
        return []
        