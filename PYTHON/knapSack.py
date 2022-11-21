def knapSack(W, wt, val, val2):
    

    if val2 == 0 or W == 0:
        return 0
 

    if (wt[val2-1] > W):
        return knapSack(W, wt, val, val2-1)
 

    else:
        return max(
            val[val2-1] + knapSack(
                W-wt[val2-1], wt, val, val2-1),
            knapSack(W, wt, val, val2-1))
 

val = [60, 100, 120]
wt = [10, 20, 30] 
W = 50
val2 = len(val)
print(knapSack(W, wt, val, val2))