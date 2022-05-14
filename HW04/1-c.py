def find_min(arr, left, right):
    if(left == right):
        return arr[left]
    if((left+1)==right):
        if ( arr[left] < arr[right] ):       
            min = arr[left]      
        else:       
            min = arr[right]
    mid = int((left + right) / 2)
    min1 = find_min(arr, left, mid)
    min2 = find_min(arr, mid+1, right)
    if(min1 < min2):
        return min1
    else:
        return min2

print("Leftmost minimum element of each row is")
arr=[[10,17,13,28,23],
    [17,22,16,29,23],
    [24,28,22,34,24],
    [11,13,6,17,7],
    [45,44,32,37,23],
    [36,33,19,21,6],
    [75,66,51,53,34]]
for i in range(0,7):
    print(find_min(arr[i],0,4))
