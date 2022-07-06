# format 함수를 사용하여 입력한 숫자의 2진수, 8진수, 16진수를 출력

from ast import Num


Number = int(input("정수를 입력해주세요: "))

print("입력한 숫자: {0:d}" .format(Number))
print("2진수 : {0:b}\n8진수 : {0:o}\n16진수 : {0:x}\n".format(Number))