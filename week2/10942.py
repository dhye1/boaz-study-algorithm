import sys
input = sys.stdin.readline

N = int(input())
num = list(input().split()) # 수열

dp = [[False] * N for _ in range(N)] # dp[i][j]는 num[i:j + 1]이 팰린드롬인지 여부를 저장

for i in range(N): # 구간이 1이면 무조건 팰린드롬
    for j in range(N):
        if i == j: 
            dp[i][j] = True

for i in range(N): # 구간이 2
    for j in range(N):
        # 두 수가 같으면
        if i + 1 == j and num[i] == num[j]: 
            dp[i][j] = True
            
for k in range(2, N): # 구간이 3 이상
    for i in range(N - k):
        # 처음과 끝 수가 같고 그 중간이 팰린드롬이라면
        if num[i] == num[i + k] and dp[i + 1][i + k - 1] == True: 
            dp[i][i + k] = True

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if dp[S - 1][E - 1]: 
      print(1)
    else: print(0)
