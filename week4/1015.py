n = int(input())
t = list(map(int, input().split()))
s_t = sorted(t)
a = []

for i in range(n):
    idx = s_t.index(t[i])
    a.append(idx)
    s_t[idx] = -1
print(*a)
