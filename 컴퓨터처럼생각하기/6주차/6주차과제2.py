# 버킷리스트 관리하기

bucketList =[]

while(True):
    num = int(input("버킷 리스트 메뉴 선택(1.추가 2.삭제 3. 보기 0.종료: "))

    if(num==1):
        bucketList.append(input("버킷 리스트에 추가할 내용: "))

    elif(num==2):
        if len(bucketList) == 0:
            print("버킷 리스트에 아무것도 없습니다!")
        else:
            bucketList.remove(input("버킷 리스트에서 삭제할 내용: "))

    elif(num==3):
        ol = 1
        for i in bucketList:
            print("%d. %s" %(ol, i))
            ol += 1

    elif(num==0):
        print("프로그램을 종료합니다.")
        break

    else:
        print("메뉴 선택 오류입니다. 다시 선택하세요.")