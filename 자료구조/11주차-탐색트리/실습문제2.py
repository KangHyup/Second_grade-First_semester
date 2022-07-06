from BSTMapClass import BSTMap

map = BSTMap()
while True :
    command = input("삽입(i), 탐색(s), 삭제(d), 출력(p), 종료(q): ")

    if command == 'i' :
        name = input("친구의 이름: ")
        phone= input("친구의 전화번호: ")
        map.insert(name, phone)

    elif command == 'd' :
        name = input("친구의 이름: ")
        map.delete(name)

    elif command == 's' :
        name = input("친구의 이름: ")
        result = map.search(name)
        if result: print("%s의 전화번호: " % name , result.value)
        else: print("등록되지 않은 친구입니다")

    elif command == 'p' :
       print("내전화번호부")
       map.display("---->")

    elif command == 'q' : break 