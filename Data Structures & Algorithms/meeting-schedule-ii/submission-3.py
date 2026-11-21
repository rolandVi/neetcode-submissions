"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        occupancy = []
        for i in intervals:
            start = i.start
            end = i.end
            
            occupancy.append([start, 1])
            occupancy.append([end, -1])
        
        occupancy.sort()

        solution = 0
        occupied = 0
        for i, val in occupancy:
            occupied += val
            solution = max(solution, occupied)
        
        return solution