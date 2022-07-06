##주의: str = str.함수 꼴이 아니므로 str은 원형유지
str = "abcd ABCD"
 
#swapcase: 대문자는 소문자로, 소문자는 대문자로
print(str.swapcase())

#upper: 소문자를 대문자로
print(str.upper())

#lower: 대문자를 소문자로
print(str.lower())

#title: 각 단어의 첫글자만 대문자로
print(str.title())

#count: 문자열에 그 단어가 몇개있는지 세어줌
print("b의 개수는: ", str.count("b"))

#find: 문자열에 그 단어가 몇번째 위치에 있는지(찾는 단어가 없으면 -1반환)
print("B의 위치는: ", str.find('B'))

#index: 문자열에 그 단어가 몇번째 위치에 있는지2(찾는 단어가 없으면 에러출력)
print("B의 위치는: ", str.index('B'))

#rfind: 문자열을 오른쪽부터 세서 몇번째 위치에 있는지(결과값은 find와 같음)
print("B의 위치는: ", str.rfind('B'))

#startwith, endswith: 문자열이 그 단어로 시작or끝나느냐 -> T or F반환
print("str은 A로 시작하나요? >>", str.startswith('A'))
print("str은 D로 끝나나요? >>", str.endswith('D'))


#strip: 문자열의 앞쪽과 뒤쪽의 공백을 제거(or 앞뒤의 특정문자를 제거)
str = " 이건 문자열임 "
print(str.strip())
print(str.strip(' 이'))

#rstrip, lstrip: 문자열의 오른쪽과 왼쪽의 공백을 제거

#replace(없앨값, 고칠값)
str = "o1o2      o3o4"
print(str.replace(' ',''))

#splite(쪼갤 기준값) 문자열을 리스트로! 바꿈
str ="하아아나 두우우울 세에엣"
print(str[0])
str = str.split()   #이제 자료형은 문자열에서 리스트가됨
print(str[0])

#자료형.join(문자열) : 문자열 사이사이에 앞의 자료형을 넣어줌 
str = "하나 둘 셋"
print('$'.join(str))

#map(함수이름, 리스트이름)