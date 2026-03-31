class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        sol = []

        for x in range(min(m+1, n+1) // 2):
            if 2*x == m-1:
                i = m -1 -x
                for j in range(x, n-x):
                    sol.append(matrix[i][j])
                break
            elif 2*x == n-1:
                j = n - 1 - x
                for i in range(x, m-x):
                    sol.append(matrix[i][j])
                break
            
            i = x
            for j in range(x, n-1-x):
                sol.append(matrix[i][j])

            j = n-1-x
            for i in range(x, m-1-x):
                sol.append(matrix[i][j])

            i = m-1-x
            for j in range(n-1-x, x, -1):
                sol.append(matrix[i][j])

            j = x
            for i in range(m-1-x, x, -1):
                sol.append(matrix[i][j])

        return sol
