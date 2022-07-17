
X = [3, 4, 56, 100, 2, 2, 3]
for x in X:
        
    try:
        summa = summa + x
    except:
        summa = x

print(summa/len(X))

