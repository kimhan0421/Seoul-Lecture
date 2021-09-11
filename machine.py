# 실습4 파이썬 자판기 만들기
# 주제 : 반복문, 제어문

# 프로그램 시나리오
# 1. 프로그램 및 사용방법 설명
# 2. 사용자 현금 입력받기
# 3. 사용자 선택 상품 입렫받기
# 4. 상품, 반환 현금 출력

# 1. 프로그램 및 사용방법 설명
print('[멋쟁이사자처럼] 커피 자판기')
print('''=======사용법=======
순서 : 현금 투입 -> 상품 선택 -> 상품 출력
구매하실 상품 번호를 입력해주세요.
상품 목록
번호 - 상품명 - 가격(원)
1 - 믹스커피 - 600
''')

item_dict = {
    '1': {
        'name': '믹스커피',
        'price': 600,
        'stock': 10
    },
    '2': {
        'name': '아아',
        'price': 1500,
        'stock': 10
    },
    '3': {
        'name': '뜨아',
        'price': 1000,
        'stock': 10
    }

}

# 2. 사용자 현금 입력받기

item_dict = dict()
while True:
    num = int(input('현금투입: '))
    item, su = input('메뉴, 수량: ').split(' ')
    # su = input('수량: ')
    su = int(su)
    # item_dict['1']['name']

    # 3. 사용자 선택 상품 입렫받기
    stock = item_dict[item]['stock']
    if stock >= su:
        name = item_dict[item]['name']
        result_num = num - (item_dict[item]['price']*su)

        # 4. 상품, 반환 현금 출력
        print(name, su, '개', '거스름돈:', result_num)
        item_dict[item]['stock'] -= su

    else:
        print('재고부족')
        break
