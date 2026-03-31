class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        sol = 0

        n = len(intervals)
        end = intervals[0][1]

        for i in range(1, n):
            s, e = intervals[i]
            if s < end:
                sol += 1
                end = min(e, end)
            else:
                end = max(e, end)
        
        return sol
                        
