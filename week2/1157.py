words = input().upper() # 모두 대문자로 변환 (대소문자 구분 없기 때문에)
unique = list(set(words)) # 입력받은 문자열에서 중복값 제거

cnt_list=[]
for i in unique:
    cnt = words.count(i)
    cnt_list.append(cnt) # count 숫자를 리스트에 append
    
if cnt_list.count(max(cnt_list)) >1 : # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list)) # count 숫자 최대값 인덱스(위치)
    print(unique[max_index])
