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