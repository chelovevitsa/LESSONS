def fib(n, l1, l2):
    if n > 0:
        n -= 1
        print(l1+l2)
        fib(n, l2, l1+l2) 


fib(10, 1, 1)
    