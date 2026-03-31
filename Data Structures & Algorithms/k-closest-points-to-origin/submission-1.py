class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            heapq.heappush(h, [p[0]**2 + p[1]**2, p])

        sol = []
        for _ in range(k):
            sol.append(heapq.heappop(h)[1])

        return sol