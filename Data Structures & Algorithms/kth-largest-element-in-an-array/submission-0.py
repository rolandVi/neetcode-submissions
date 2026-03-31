class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            if len(pq) < k:
                heapq.heappush(pq, i)
                continue

            value = heapq.heappop(pq)

            heapq.heappush(pq, max(i, value))
        
        return heapq.heappop(pq)