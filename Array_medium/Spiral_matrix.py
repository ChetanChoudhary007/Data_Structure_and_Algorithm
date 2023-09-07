class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # declared the rows and cols
        m=len(matrix)
        n=len(matrix[0])

        # return list
        final_list=[]
        
        # intialize required pointer
        top=0
        right=n-1
        bottom=m-1
        left=0

        # main algorithms
        while top <= bottom and left <=right:

            # adding as we move from left to right
            for r in range(left,right+1):
                final_list.append(matrix[top][r])
            top+=1

            # adding elements as we move top tp bottom
            for d in range(top,bottom+1):
                final_list.append(matrix[d][right])
            right-=1
            
            #adding elements as we move right to left
            if top <=bottom:
                for l in range(right,left-1,-1):
                    final_list.append(matrix[bottom][l])
                bottom-=1

            #adding elements as we move bottom to top
            if left <= right:
                for u in range(bottom,top-1,-1):
                    final_list.append(matrix[u][left]) 
                left+=1
            
        
        #return the final list 
        return final_list