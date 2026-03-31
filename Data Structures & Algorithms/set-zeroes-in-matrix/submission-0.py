class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        rows = defaultdict(int)
        cols = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if rows.get(i, 1) == 0 or cols.get(j, 1) == 0:
                        matrix[i][j] = 0
        return