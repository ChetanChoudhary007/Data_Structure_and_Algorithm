class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # declared the length of the matrix
        m=len(matrix)
        n=len(matrix[0])

        # create an temporary variable that stores the marked value of a[0][0]
        col0= 1

        # mark matrix at first row and first columns
        for i in range(m):
            for j in range(n):
                if matrix [i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        
        # iterate the matrix
        for i in range(1,m):
            for j in range(1,n):
                #check if the matrix[0][0] is '0' or not
                if matrix[i][j]!=0:
                    if matrix[0][j]==0 or matrix[i][0]==0:
                        matrix[i][j]=0
            
        #for 1st row and col
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0
        if col0==0:
            for i in range(m):
                matrix[i][0]=0