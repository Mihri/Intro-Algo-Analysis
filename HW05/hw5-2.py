def ActivitySelection(start, finish, n):
    print("The optimal list of sessions:");
    j = 0
    count=1
    print("(",start[j],"-",finish[j],")")
    for i in range(1,n):
        if start[i] >= finish[j]:
            print("(",start[i],"-",finish[i],")")
            j = i
            count=count+1
    print("\nMaximum number of sessions-->",count)

start = [1, 3, 2, 0, 5, 8, 11]
finish = [3, 4, 5, 7, 9, 10, 12]
n = len(start)
ActivitySelection(start, finish, n)
