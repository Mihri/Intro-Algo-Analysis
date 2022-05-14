def subSum(arr, targetSum):

    j=0
    k=0
    m=0
    pSum=0
    nSum=0
    positive={}
    negative={}
    nonZeros={}
    lookup_table={}
    
    for i in range(0,(len(arr))):
        if arr[i]>0:
            positive[j]=arr[i]
            nonZeros[m]=arr[i]
            j=j+1
            m=m+1
        if arr[i]<0:
            negative[k]=arr[i]
            nonZeros[m]=arr[i]
            k=k+1
            m=m+1
    
    for i in range(0,(len(positive))):
        pSum += positive[i]
    for i in range(0,(len(negative))):
        nSum += negative[i]
  
    def subSumX(index, goal):
        if goal < nSum or goal > pSum:
            return False

        if index == 0:
            return nonZeros[0] == goal

        key = (index, goal)
        if key in lookup_table:
            return lookup_table[key]

        result = nonZeros[index] == goal or subSumX(index-1, goal) or subSumX(index-1, goal-nonZeros[index])

        lookup_table[key] = result
        return result
    
    return subSumX(len(nonZeros)-1, targetSum)

arr = [1, 3, -3, 5, 7]
result = subSum(arr, 0)
if result==True:
    print('The set has a subset sum of 0.')
else:
    print('The set does not have a subset sum of 0')
