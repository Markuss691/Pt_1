X = [3, 4, 56, 100, 15, 2, 20, 30]

P = 1


for x in X:
    if int(x/3) == float(x/3) or int(x/5) == float(x/5):
        P = P * x    
    
  
print(P)

