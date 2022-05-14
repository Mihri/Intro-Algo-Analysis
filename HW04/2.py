def find_kth_elementh(arrA,arrB,k):    
        if len(arrA) == 0:
            return arrB[k]
        if len(arrB) == 0:
            return arrA[k]
        
        midA = len(arrA)//2
        midB = len(arrB)//2
        
        if midA + midB < k:
            if arrA[midA] > arrB[midB]:
                return find_kth_elementh(arrA,arrB[midB+1:], k-midB-1)
            else:
                return find_kth_elementh(arrA[midA+1:],arrB, k-midA-1)
        else:
            if arrA[midA] > arrB[midB]:
                return find_kth_elementh(arrA[:midA],arrB, k)
            else:
                return find_kth_elementh(arrA,arrB[:midB], k)

arrA = [1,3,5,7,9]
arrB = [2,4,6,8]

for i in range(1,10):
    output = find_kth_elementh(arrA,arrB,i-1)
    print(output)

