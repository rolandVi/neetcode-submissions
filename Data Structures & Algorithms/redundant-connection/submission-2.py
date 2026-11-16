class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return [a, b]  # Already connected -> this edge creates the cycle
            parent[root_a] = root_b