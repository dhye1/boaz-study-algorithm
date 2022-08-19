def fib(n):
    if n < 2:
        return n
    num = fib(n-1)+fib(n-2)
    return num
n = int(input())
print(fib(n))
    
