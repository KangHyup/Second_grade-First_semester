#딕셔너리: 키와 값의 묶음들

dict1 = {'이름': '홍길동', '나이':25, '연락처':'010-1234-5678'}
print(dict1)

#키를 이용해 값을 변경가능
dict1['이름'] = '구창모'
print(dict1['이름'])

#새로운키로 데이터 추가
dict1['주소'] = '덕소'
print(dict1)

#get(키): 키에 해당하는 값을 반환
print(dict1.get('이름'));   print(dict1['이름']) #둘은 같은표현, 괄호에 주의할것

#key(): 딕셔너리의 모든 키를 튜플형태로 반환
print(dict1.keys())

#list(): key()할때 앞에 생성되는 dict_keys라는 문구를 지워주고 배열 형식으로 만들어줌
print(list(dict1.keys()))
keys = list(dict1.keys())

#values(): 딕셔너리의 값들을 튜플형태로 반환
print((dict1.values()))

#item(): 딕셔너리의 모든 키와 값들을 튜플형태로 반환
print((dict1.items()))

#in : 딕셔너리에 키가 있으면 True, 없으면 False
print('이름' in dict1, '성별' in dict1)


##사용예시
#빈 딕셔너리선언
rapper = {}

rapper['이름'] = '구창모'
rapper['고향'] = '덕소'
rapper['히트곡'] = 'Meteor'

#키값의 갯수만큼 반복
for i in rapper.keys():
    print('%s: %s' % (i, rapper[i]))


