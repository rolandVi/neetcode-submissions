class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [set() for i in range(numCourses)]
        in_degrees = [0 for i in range(numCourses)]

        for to, fro in prerequisites:
            adj_list[fro].add(to)
            in_degrees[to] += 1
        
        q = deque([])
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for neighbour in adj_list[node]:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    q.append(neighbour)
        
        for degree in in_degrees:
            if degree > 0:
                return False
        return True
