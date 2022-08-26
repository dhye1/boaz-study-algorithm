import sys

input = sys.stdin.readline
N, M = map(int, input().split())

aSet = {input().rstrip() for _ in range(N)}
bSet = {input().rstrip() for _ in range(M)}
abList = list(aSet & bSet) 
abList.sort()

print(len(abList))
for i in abList:
    print(i)
