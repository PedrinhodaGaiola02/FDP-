
a0 = 0
a1 = 1

def fib(k):
    if k == 0:
        a = 0
    elif k == 1:
        a = 1
    else: 
        a = k -1 + k -2
    return a


a2 = fib(2)
print(a2)