a = []
for i in range(int(input())):
    a.append(int(input()))

cnt = 0
while True:
    is_True = True
    for i in range(1, len(a)):
        if a[i] >= a[0]:
            is_True = False
            break
    if is_True:
        print(cnt)
        break
    else:
        for i in range(1, len(a)):
            if a[i] == max(a):
                break
        a[i] -= 1
        cnt += 1
        a[0] += 1
