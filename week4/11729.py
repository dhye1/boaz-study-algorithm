def hanoi(n,a,c,b):
    if n == 1:
        print(a,c)
        return
    hanoi(n-1,a,b,c)
    print(a,c)
    hanoi(n-1,b,c,a)
    
n = int(input())
print(2**n-1)
hanoi(n,1,3,2)
