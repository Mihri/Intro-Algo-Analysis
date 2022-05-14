def MinCost(n,M,NY,SF):
    opSF = 0
    opNY = 0

    for i in range(1, n):
        minSF = opSF
        minNY = opNY
        opSF = SF[i] + min(minSF,M+minNY)
        opNY = NY[i] + min(minNY,M+minSF)

    return min(opSF,opNY)

NY = [0, 1, 3, 20, 30] 
SF = [0, 50, 20, 2, 4]
n = 4  
M = 10 
print("Total minimum cost:",MinCost(n + 1,M,NY,SF))
