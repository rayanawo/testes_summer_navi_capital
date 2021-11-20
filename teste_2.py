import math

X = []

def fatorial(n):
    if n == 1 or n == 0: 
        return 1
    
    else:
        return n * fatorial(n-1)


for i in range(1, 11):
    
    if i % 2 == 0:
        X.append( round((3 + 7 * (fatorial(i))), 2) )
    
    else:
        X.append( round((math.pow(2,i) + 4 * math.log(i)), 2) )


print(X)