X = int(input())
H = int(input())
M = int(input())
X1 = (X+(H*60)+M)
Y = (X1%60)
X2 = (X1//60)
print(X2)
print(Y)