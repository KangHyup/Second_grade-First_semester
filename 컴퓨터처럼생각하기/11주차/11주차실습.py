class BankAccount():
    def __init__(self):
        self.money = 0

    def deposit(self, howmuch):
        self.money += howmuch
        print("통장에 %d가 입금되었음" %howmuch)

    def withdraw(self, howmuch):
        if(self.money < howmuch):
            print("출금할 돈이 부족함")
        
        else:
            self.money -= howmuch
            print("통장에 %d가 출금되었음" %howmuch)
            print("남은잔액: %d" %self.money)