
X = range(0,88888888)
for x in X:
   # print(x)
    try:
        summa = summa + x
    except NameError:
        summa = x

print(summa)
