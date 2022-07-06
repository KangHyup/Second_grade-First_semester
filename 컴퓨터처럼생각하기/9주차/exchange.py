
def exchange_search():
    print("-"*35)
    print("미국 - 1215.5달러")
    print("영국 - 1595.53파운드")
    print("러시아 - 11.6루블")
    print("중국 - 190.66위안")
    print("유럽연합 - 1341.67유로")
    print("-"*35)

def clac_money(n, m):
    moneyInfo= {"미국":(1215.50,"달러"),"영국":(1595.53,"파운드"),"러시아":(11.67,"루블"),"중국":(190.66,"위안"),"유럽연합":(1341.67,"유로")}

    if (n in moneyInfo.keys()):
        rate,unit=moneyInfo.get(n)
        
    else: 
        print("국가를 잘못 입력 했습니다.")
        return 

    result = m/rate
    print("%d(원)dmf :%.2f(%s)로 교환합니다" %(m, result, unit))
