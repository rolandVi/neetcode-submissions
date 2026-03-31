class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for fro, to in tickets:
            adj[fro].append(to)

        for key in adj:
            adj[key].sort(reverse = True)
        
        sol = []
        def dfs(curr: str) -> None:
            while len(adj.get(curr, [])) > 0:
                next_node = adj[curr][-1]
                adj[curr].pop()

                dfs(next_node)

            sol.append(curr)

        dfs("JFK")
        sol.reverse()
        return sol