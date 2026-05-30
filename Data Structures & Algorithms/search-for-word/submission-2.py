class SolutionMine:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [[0,1], [1,0], [0, -1], [-1, 0]]
        n, m = len(board), len(board[0])

        def valid(i: int, j: int) -> bool:
            return i >= 0 and i < n and j >= 0 and j < m

        def dfs(i: int, j: int, index: int, seen: Set[int]) -> bool:
            if index == len(word):
                return True

            result_found = False
            seen.add(i*m + j)
            for di, dj in direction:
                if valid(i + di, j + dj) and ((i+di) * m + (j+dj) not in seen) and board[i+di][j+dj] == word[index]:
                    result_found |= dfs(i+di, j+dj, index+1, seen)
            
            seen.remove(i*m + j)
            return result_found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 1, set()):
                    return True

        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False