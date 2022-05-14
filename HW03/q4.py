def insertionSort(a):
    
    for i in range(1, len(a)): 
  
        key = a[i]  
        j = i-1
        while j >=0 and key < a[j] : 
                a[j+1] = a[j] 
                j -= 1
        a[j+1] = key 

def findMedian(a, n): 

    if n % 2 != 0: 
        return float(a[int((n-1)/2)]) 
      
    return float((a[int((n-1)/2)] + a[int(n/2)])/2.0) 
  

arr = [2, 4, 7, 5, 22, 11] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 
n = len(arr) 
#print(n)
print("Median =", findMedian(arr, n)) 
