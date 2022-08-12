a= int(input())
b= int(input())
c= int(input())

k = a*b*c
k_list = list(str(k))

for i in range(10):
    count = k_list.count(str(i))
    print(count)
