#메뉴주문후 가격을 알려주는 프로그램

price = 0
select = 99
howmany = 0
print("[1]떡볶이 [2]튀김 [3]핫도그 [4]음료")
print("주문을 끝내려면 [0]을 입력하세요")
print("--------------------------------")

while(True):
    select = int(input("선택메뉴 : "))
    if select <0 or select>4:
        print("메뉴선택 오류...다시선택하세요")
    elif select == 0:
        print("---------------")
        break
    
    else:
        howmany = int(input("주문수량 : "))
        if select == 1: price+=4500*howmany
        elif select == 2: price+=4000*howmany
        elif select == 3: price+=2500*howmany
        elif select == 4: price+=1500*howmany

print("금액 합계는 %d원 입니다." % price)
