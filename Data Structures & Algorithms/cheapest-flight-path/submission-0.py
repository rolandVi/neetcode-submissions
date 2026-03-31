class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for fro, to, price in flights:
            adj_list[fro].append([to, price])

        min_steps = [float('inf') for _ in range(n)]
        visited = [False for _ in range(n)]

        pq = [] # [distance, steps, id]
        heapq.heappush(pq, [0, 0, src])

        while pq:
            length, steps, cur = heapq.heappop(pq)

            if steps > k + 1:
                continue
            if visited[cur] and steps >= min_steps[cur]:
                continue

            min_steps[cur] = min(min_steps[cur], steps)
            visited[cur] = True

            if cur == dst and steps <= k+1:
                return length

            for nei, cost in adj_list[cur]:
                if steps + 1 < min_steps[nei]:
                    heapq.heappush(pq, [length + cost, steps + 1, nei])

        return -1