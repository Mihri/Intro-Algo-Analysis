def isBipartite(arr, visited, c, loc):  
      
    if visited[loc] != -1 and visited[loc] != c:  
        return False 
          
    visited[loc] = c  
    result = True 
    for i in range(0, N):  
        if arr[loc][i]:  
            if visited[i] == -1:  
                result &= isBipartite(arr, visited , 1-c , i)  
                  
            if visited[i] !=-1 and visited[i] != 1-c:  
                return False 
           
        if not result:  
            return False 
       
    return True

N=4
arr = [[0, 1, 0, 1],  [1, 0, 1, 0],  [0, 1, 0, 1],  [1, 0, 1, 0]]  
visited = [-1] * N    
 
if isBipartite(arr, visited, 1, 0):
    print("Given graph is a bipartite graph!")  
else:
    print("Given graph is not a bipartite graph!")
