import math

lb = []

n = 100
for x in range(2, int(n**(0.5)+1)):
    if x not in lb:
        print(x)
        for y in range(x,n+1):
            if y % x == 0:
                lb.append(y)

for x in range(2, n+1):
    if x not in lb:
        print(x)
