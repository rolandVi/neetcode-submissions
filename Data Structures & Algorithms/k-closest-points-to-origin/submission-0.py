class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            heapq.heappush(h, [self.dis(p), p])

        sol = []
        for _ in range(k):
            sol.append(heapq.heappop(h)[1])

        return sol
        
    def dis(self, a: List[int]) -> float:
        return math.sqrt(a[0]**2 + a[1]**2)