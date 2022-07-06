
shop = {"가치킨":2000, "나중국집":3000, "다분식":2500, "라족발":4000, "마커피":3000, "바횟집":5000, "사돈까스":4000, "아도시락":1500, }

highshop = ''
lowshop = ''
high = 0
low  = 9999

for i in shop:
    if shop[i] > high: 
        highshop = i
        high = shop[i]
    if shop[i] < low: 
        lowshop = i
        low = shop[i]

print("배달료 가장 비싼 가게: %s - %d" % (highshop, high))
print("배달료 가장 싼 가게: %s - %d" % (lowshop, low))
