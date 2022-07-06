##파이썬에서 SQLite 사용하는 방법

#1. 데이터 베이스 연결
import sqlite3
#connect("경로") -> 경로에 파일이 있다면 연결을, 없으면 새로생성
con = sqlite3.connect("C:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/13주차-데이터베이스/naverDB")

#2. 커서생성(연결통로)
cur = con.cursor()

cur.execute("CREATE TABLE userTable(id char(4), userName char(15), email char(15), birthYear int)") #만약 데이터베이스파일이 없다면 일단 만들어야함


#3. 테이블만들기(sqlite3에서 실행했던것 그대로 쳐주면 됨)
cur.execute("CREATE TABLE userTable(id char(4), userName char(15), email char(15), birthYear int )") #CREATE TABLE 테이블이름(넣을 데이터 자료형)

#4. 데이터 입력
cur.execute("INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('hyup', 'Kang Hyup', 'hyup98@naver.com', 1998)")
cur.execute("INSERT INTO userTable VALUES('lee', 'Lee Sa Su', 'AMD@naver.com', 1984)")
cur.execute("INSERT INTO userTable VALUES('park', 'Park Kun', 'Pakr@naver.com', 2002)")

#5. 입력한 데이터 저장
con.commit()

#5. 데이터베이스 닫기
con.close()