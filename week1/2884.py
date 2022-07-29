a,b = map(int, input().split())
if b>=45:
    print(a,end=' ')
    print(b-45)
else:
    if a == 0:
        print(23,end=' ')
        print(b+15)
    else:
        print(a-1, end=' ')
        print(b+15)
