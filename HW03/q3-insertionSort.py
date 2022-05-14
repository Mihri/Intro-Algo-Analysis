def insertionSort(a): 
    count = 0
    for i in range(1, len(a)): 
  
        key = a[i] 
        j = i-1
        
        while j >=0 and key < a[j] : 
                a[j+1] = a[j] 
                j -= 1
                count=count+1
                
        a[j+1] = key
    print("Number od swapping is:")
    print(count)

a = [22, 11, 7, 5, 4, 2] 
insertionSort(a) 
print ("Sorted array is:") 
for i in range(len(a)): 
    print ("%d" %a[i])
