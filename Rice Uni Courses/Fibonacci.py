def fibo(alist, iter):
    for i in range(iter):
        alist.append(alist[-1]+alist[-2])
    return alist


print(fibo([0, 1], 20))
