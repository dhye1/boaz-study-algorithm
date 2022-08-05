def solve(a):
    cnt = 0
    for i in range(1,a+1):
        num_list = list(map(int,str(i))) # ['2','3','4'] -> [2,3,4]
        if 1<=i<100:
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1
    return cnt

n = int(input())
print(solve(n))
