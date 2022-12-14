import sys
from collections import Counter


N=int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

#1 산술 평균 (소수점 첫 번째 자리에서 반올림)
print(round(sum(arr)/N))

#2 중앙값
arr.sort()
print(arr[N//2])

#3 최빈값
k=Counter(arr).most_common()


if len(arr) > 1:  #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0])
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else:
        print(k[0][0])
else:
    print(arr[0])

#4 범위
print(arr[-1] -  arr[0])
