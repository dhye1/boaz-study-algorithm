def d(n): # 생성자 n으로부터 d(n) 구하는 수식
    n = n + sum(map(int,str(n)))
    return n

#셀프 넘버가 아닌 수(생성자 있는 수)들의 집합. 겹치는 것 제외하기 위해 set()
nonSelfNum = set()

# nonSelfNum에 들어갈 수 넣기
for i in range(1, 10001):
    nonSelfNum.add(d(i))

# 셀프 넘버 출력
for i in range(1,10001):
    if i not in nonSelfNum:
        print(i)
