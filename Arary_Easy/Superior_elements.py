class Solution:
    def superiorElements(a : list[int]) -> list[int]:
        # declare the size of array
        n=len(a)

        # declare the final empty array
        final_a=[]

        # append the array that superrior 
        right=0
        for i in range(n-1,-1,-1):
            if a[i] > right:
                final_a.append(a[i])
                right=a[i]
            else:
                continue

        # return the list that contain only superior elements
        return final_a