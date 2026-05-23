class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = [0 for _ in range(n)]

        def dfs(node: int) -> None:
            visited[node] = 1
            for nei in adj_list[node]:
                if not visited[nei]:
                    dfs(nei)

        dfs(0)
        
        return sum(visited) == n