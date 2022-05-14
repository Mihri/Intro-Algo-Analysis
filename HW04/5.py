import numpy as cal
price = cal.array([7,9,5,21,7,13,10,14,20]) 
cost = cal.array([5,11,2,21,5,7,8,12,13]) 
   
print ("Price :", price) 
print ("Cost : ", cost) 
   
gain = cal.subtract(price, cost)  
print ("Gain : ", gain)

    
def check(arr, val): 
    return(all(i <= val for i in arr)) 
val = 0 
if(check(gain, val)): 
    print("There is no day to make money")


def find_max(arr, left, right):
    if(left == right):
        return left+1
    if((left+1)==right):
        if ( arr[left] < arr[right] ):       
            max = arr[right]      
        else:       
            max = arr[left]
    mid = int((left + right) / 2)
    max1 = find_max(arr, left, mid)
    max2 = find_max(arr, mid+1, right)
    if(max1 > max2):
        return max1
    else:
        return max2
    
print("The best day to buy the goods is",find_max(gain, 0, len(gain)-1),"st day")



