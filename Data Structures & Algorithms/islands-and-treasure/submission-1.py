class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque() # [i, j]
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def valid(a: int, b: int) -> bool:
            return a >= 0 and a < m and b >= 0 and b < n
        
        while q:
            i, j = q.popleft()

            for x, y in directions:
                ni, nj = i + x, j + y
                if valid(ni, nj) and grid[ni][nj] != -1 and grid[i][j] + 1 < grid[ni][nj]:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append([ni, nj])
        return
                    
