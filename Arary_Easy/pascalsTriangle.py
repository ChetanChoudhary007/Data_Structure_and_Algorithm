class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans=1
        final_list=[[1]]
        for i in range(2,numRows+1):
            row=[1]*i
            if i > 2:
                ans=1
                for j in range(1,len(row)-1):
                    ans=ans*(len(row)-j)
                    ans=ans//j
                    row[j]=ans
                final_list.append(row)
            else:
                final_list.append(row)

        return final_list