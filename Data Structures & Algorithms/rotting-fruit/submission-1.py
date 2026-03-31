class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m = len(grid)
        n = len(grid[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])

        if fresh == 0:
            return 0

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def valid(a: int, b: int) -> bool:
            return a >= 0 and a < m and b >= 0 and b < n

        time = -1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in directions:
                    ni, nj = i + x, j + y

                    if valid(ni, nj) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append([ni, nj])
            time += 1

        if fresh > 0:
            return -1

        return time