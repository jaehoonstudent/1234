# 12월 24일
try :
    a = 3 / 0
except ZeroDivisionError: # elif
    print("aaa")
except  : # else
    print("bbb")

# raise
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try :
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration
except StopIteration :
    print("종료")

# 논리연산
# or and
# 0은 False , 나머지는 True
# bool = true랑 false를 가지고 있음
# or 는 하나만 T면 T
# and 는 둘다 T여야 T
if 1:
    print("1입니다.")

# 리스트
list1 = [135, 462, 27, 2753, 234]
print(list1.index(27))   #2가 출력

#slice 자르다
text = "hello world"
text[1:5]  #1~4   # ello          1번째부터 5번째 전까지
text[3:]          # lo world      3번째부터 끝까지
text[:3]          # hel           처음부터 3번째까지
text[:]           # hello world   처음부터 끝까지