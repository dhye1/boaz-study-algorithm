n = int(input())
for i in range(n):
    m = list(map(int,input().split()))
    avg = sum(m[1:])/m[0]
    c = 0
    for k in range(1,len(m)):
        if m[k] > avg:
            c+=1
    ratio = c/m[0]*100
    print(f'{ratio:.3f}%')
