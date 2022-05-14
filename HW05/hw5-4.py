class Value:
    def __init__(self, match, mismatch, gap):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

def findAlign(Str1, Str2, value=Value(2, -2, -1)):
    arr = [[0]*(len(Str2) + 1) for i in range(len(Str1) + 1)]
    cost = 0
    for i in range(1, len(Str2)):
        for j in range(1, len(Str1)):
            arr[i][j] = max(arr[i][j-1] + value.gap,arr[i-1][j] + value.gap,arr[i-1][j-1] + (value.match if Str1[i] == Str2[j] else value.mismatch),0)

        if arr[i][j] >= cost:
            cost = arr[i][j]
    return cost

print(findAlign("alignme", "sli  me",value=Value(2, -2, -1)))
