n = int(input())
book= []
unique_list=[]

for _ in range(n):
    book.append(input())

for x in book:
    if x not in unique_list:
        unique_list.append(x)

cnt =[book.count(x) for x in unique_list]
idx = []

for i in range(len(cnt)):
    if cnt[i]==max(cnt):
        idx.append(i)

print(sorted([unique_list[i] for i in idx])[0])
