class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        
        # using zip function
        # matrix[:]=list(zip(*matrix[::-1]))

        ##Using rows exchange approach 

        #declared the rows and columns
        m=len(matrix)

        # iterate the matrix and exchange rows
        up=0
        down=m-1
        while up < down:
            matrix[up],matrix[down]=matrix[down],matrix[up]
            up+=1
            down-=1
        
        #exchange the values in each rows
        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]