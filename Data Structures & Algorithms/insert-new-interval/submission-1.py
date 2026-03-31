class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        sol = []
        n = len(intervals)
        if n == 0:
            return [newInterval]

        if s < intervals[0][0] and e < intervals[0][0]:
            sol.append([s, e])
            sol += intervals
            return sol
        if s > intervals[n-1][1] and e > intervals[n-1][1]:
            sol += intervals
            sol.append([s, e])
            return sol

        if s < intervals[0][0] and e >= intervals[0][0]:
            e = intervals[0][1]
        
        for i in range(n):
            if s < intervals[i][0] and e < intervals[i][0]:
                sol += intervals[i:]
                break

            if s > intervals[i][1] and e > intervals[i][1]:
                sol.append(intervals[i])
                continue
            if s > intervals[i][1] and e < intervals[i+1][0]:
                sol.append([s, e])
                continue
            
            if s <= intervals[i][1]:
                s = intervals[i][0]
            while i < n-1 and e >= intervals[i+1][0]:
                e = max(intervals[i+1][1], e)
                i += 1
            
            sol.append([s, e])

        return sol

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        sol = []
        n = len(intervals)
        if n == 0:
            return [newInterval]

        i = 0
        while i < n and s > intervals[i][1]:
            sol.append(intervals[i])
            i += 1
        if i == n:
            sol.append([s, e])
            return sol

        s = min(s, intervals[i][0])

        while i < n and e >= intervals[i][0]:
            e = max(e, intervals[i][1])
            i += 1
        sol.append([s, e])

        sol += intervals[i:]

        return sol