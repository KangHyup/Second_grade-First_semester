#리스트에서 사용할수 있는 함수들
aa = []

#append(값): 리스트에 값추가
aa.append('A')
aa.append('C')
aa.append('B')

#sort(): 리스트의 항목을 정렬
aa.sort()
print(aa)

#reverse(): 리스트항목을 역순으로 정렬
aa.reverse()
print(aa)

#index(값): 값을 입력하면 그게 몇번째 있는건지 알려줌
print(aa.index("B"))

#insert(위치, 값): 값을 n번째위치로 삽입
aa.insert(1,"D")

#len(리스트이름): 리스트의 길이를 정수형으로 반환 주의할건 aa.len()이 아닌 len(aa)
print(len(aa), type(len(aa)))

#count(값): 리스트에 중복된 값의 갯수가 몇개인지 알려줌
print(aa.count('A'))

#remove(값): 값을 지운다. 위치를 주는게아니라 값을 주는게 포인트. 만약 리스트에 값이 중복되어있을경우 첫번째것만 지운다
aa.remove('A')

#del(리스트이름[위치]): 해당위치의 항목을 지운다 aa.del()이 아니라 del(aa[0])이다
del(aa[0])

#pop: 맨뒤의 항목을 빼고, 뺀건 삭제
aa.pop()

#extend(리스트): 리스트끼리 합침, 리스트+리스트와 같음
B = [10, 20, 30]
print(aa + B)   # 연산후에도 aa는 [D]임
aa.extend(B)    # 연산후에는 aa는 [D,10,20,30]임
print(aa)