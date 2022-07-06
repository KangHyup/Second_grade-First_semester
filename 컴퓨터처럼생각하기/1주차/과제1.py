# 물건의 원가와 부가세를 계산하기
# 부가세는 소비가의 10%

Price = int(input("결제 금액을 입력해주세요. :"))

tax = Price/11
Realprice = Price - tax
print("결제 금액", Price, "원은 상품 가격", Realprice, "원과 부가세", tax, "원의 합계입니다.")

