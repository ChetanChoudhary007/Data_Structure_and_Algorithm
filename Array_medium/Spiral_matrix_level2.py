class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:

        # create the matrix
        matrix=[[0 for i in range(n)]for i in range(n)]
        marker=0

        # list that stores the values
        till_n=[i for i in range(1,n**2+1)]

        #main algorithms
        top=0
        left=0
        right=n-1
        bottom=n-1

        while top <= bottom and left <=right:

            #filling the elements in top row
            for r in range(left,right+1):
                val=till_n[marker]
                marker+=1
                matrix[top][r]=val
            top+=1

            #filling the elements in right column
            for d in range(top,bottom+1):
                val=till_n[marker]
                marker+=1
                matrix[d][right]=val
            right-=1

            #filling the elements in the bottom row 
            if top <=bottom:
                for l in range(right,left-1,-1):
                    val=till_n[marker]
                    marker+=1  
                    matrix[bottom][l]=val
            bottom-=1

            #filling the elements in the left row
            if left <= right:
                for u in range(bottom,top-1,-1):
                    val=till_n[marker]
                    marker+=1
                    matrix[u][left]=val
            left+=1

        return matrix