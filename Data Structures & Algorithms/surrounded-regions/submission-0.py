

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dire = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = set()

        def valid(i: int, j: int) -> bool:
            return i >=0 and i < m and j>=0 and j < n
        
        def dfs(i: int, j: int, region: Set[tuple[int, int]]) -> None:
            region.add((i, j))

            for x, y in dire:
                newi, newj = i + x, j + y
                if not valid(newi, newj):
                    nonlocal surr 
                    surr = False

                elif board[newi][newj] == "O" and (newi, newj) not in region:
                    dfs(newi, newj, region)
            return

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in seen:
                    region = set()
                    surr = True

                    dfs(i, j, region)

                    seen.update(region)
                    if surr:
                        for y, x in region:
                            board[y][x] = "X"

        return
