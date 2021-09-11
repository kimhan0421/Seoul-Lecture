vDict = {'Kim': 1984, 'Choi': 1999, 'Lee': 2000, 'Park': 1980}
itemlist = vDict.items()  # item()이라는 딕셔너리(Dictionary)의 내장함수
#  Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다
item_key = vDict.keys()
item_values = vDict.values()

print(itemlist)
# print('v', item_key)
# print('values', item_values)

for item in itemlist:
    print(item)
