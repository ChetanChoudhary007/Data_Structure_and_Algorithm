def missingAndRepeating(arr:list, n:int)-> list:
    
    # Initialize the return variables
    repeat=0
    missing=0
    
    # list that track the count of element and missing element in the given list
    visited=[0]*(n+1)
    
    # main logic
    for i in arr:
        visited[i]+=1 
    
    for i in range(1,len(visited)):
        if visited[i] >1:
            repeat=i
        if visited[i] ==0 :
            missing=i
    
    # return the missing and repeated number
    return [missing,repeat]
