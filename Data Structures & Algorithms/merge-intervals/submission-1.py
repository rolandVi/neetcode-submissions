class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        sol = []

        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            
            while i+1 < n and end >= intervals[i+1][0]:
                i += 1
                end = max(intervals[i][1], end)
            

            sol.append([start, end])
            i += 1

        return sol