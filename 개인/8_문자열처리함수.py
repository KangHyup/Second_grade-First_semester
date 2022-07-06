##문자열 처리함수

python = "Python is Amazing"

# 문자열을 소문자로 lower
print(python.lower())

# 문자열을 대문자로 upper
print(python.upper())

# 특정 문자열의 위치가 대문자인가? isupper
print(python[0].isupper()) #True

# 문자열의 길이 len
print(len(python))

# 특정문자만 바꾸기 replace
print(python.replace("Python", "Java"))

# 특정글자가 몇번째에 있는가? index
index = python.index("n")
print(index)
index = python.index("n", index + 1) # index(=5)+1 번째 위치, 즉 6번째이후 부터 n을 찾음
print(index)

# index와 유사한 find
print(python.find("n"))
print(python.find("Java")) #포함되어있지 않은 글자가 있으면 -1반환 *index의 경우 오류가 나옴*

# 글자가 몇번 나온지 알려주는 count
print(python.count("n"))
