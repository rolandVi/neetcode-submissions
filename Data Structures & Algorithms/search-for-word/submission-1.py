class Solution:
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