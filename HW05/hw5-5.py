def findSum(a):    
    n = len(a)
    sum=0
       
    i = n - 1
    while(i >= 0):
        if(a[i]<0):
            sum=sum-a[i]
        else:
            sum=sum+a[i]
        i -= 1
        
    print(sum)

arr = [-1, 2, 5, 10]   
print("Sum of the array with the minimum number of operations: ", end = "") 
findSum(arr) 

