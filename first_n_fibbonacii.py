def first_n_fibo(n):
    ls = [1]*n
    for i in range(2,len(ls)):
        ls[i] = ls[i-1]+ls[i-2]

    return ls

print(first_n_fibo(5))