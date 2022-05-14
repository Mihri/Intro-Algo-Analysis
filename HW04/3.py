def maxSub(arr):
    
    #Base Case: If there is one element in the array
    if len(arr) == 1:
        if arr[0] > 0:
            return []
        return arr

    #Dividing the array and calculating them
    LeftArr = arr[:len(arr)//2]
    maxLeftSub = maxSub(LeftArr)
    RightArr = arr[len(arr)//2:]
    maxRightSub = maxSub(RightArr)

    #For Left
    midLeftSum = 0
    midLeftSumId = len(LeftArr)
    temp = 0
    for i in range(len(LeftArr)-1, -1, -1):
        temp += LeftArr[i]
        if temp > midLeftSum:
            midLeftSum = temp
            midLeftSumId = i
            
    #For Right
    midRightSum = 0
    midRightSumId = 0
    temp = 0
    for i in range(len(RightArr)):
        temp += RightArr[i]
        if temp > midRightSum:
            midRightSum = temp
            midRightSumId = i

    sums = [sum(maxLeftSub) , midLeftSum+midRightSum ,sum(maxRightSub)]
    maxSum = max(sums)
    
    if maxSum == sums[0]:
        return maxLeftSub
    elif maxSum == sums[1]:
        return arr[midLeftSumId:len(LeftArr)+midRightSumId+1]
    else:
        return maxRightSub
 
inputArr = [5, -6, 6, 7, -6, 7, -4, 3]
output = maxSub(inputArr)
print("The contiguous subset with the largest sum is", output,"whose sum is ",sum(output))

