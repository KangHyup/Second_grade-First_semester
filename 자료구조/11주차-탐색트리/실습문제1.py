from http.client import ImproperConnectionState
from BSTMapClass import BSTMap

map = BSTMap()
data =  [11,3,4,1,56,5,6,2,98,32,23]

print("[삽입연산]: ", data)
for key in data:
    map.insert(key)
map.display("[중위순회]: ")