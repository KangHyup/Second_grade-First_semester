import exchange


exchange.exchange_search()

while(True):
    money = int(input("환전하려는 금액(원):"))
    country = input("국가(미국/영국/러시아/중국/유럽연합):")
    exchange.clac_money(country, money)
