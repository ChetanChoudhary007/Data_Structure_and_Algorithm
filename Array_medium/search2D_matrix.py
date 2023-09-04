class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        for i in range(m):
            n=len(matrix[i])
            for j in range(n):
                if matrix[i][j]==target:
                    return True