
def fib(k):
    if (k == 0):
        a = 0
        return a
    if (k == 1):
        a = 1
        return a
    if (k >> 1):
        a = fib(k -2)+ fib(k -1)
        return a

sequencia  = []

k = 25

for i in range(k + 1):
    sequencia.append(fib(i))
    print(sequencia)





