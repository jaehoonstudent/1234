# 파이썬
# 주석 처리
# 변수
a = 10
b = 1.1
print(a)
print(b)

c = '조재훈'
c = '조재웅'
print(c + c) # 조재웅조재웅
print("조재훈") # 조재훈

# 변수 : 변하는 수의 약자

# 반복문
# C언어 묶어줄 때 { }
# 파이썬은 들여쓰기
# for 반복문
for i in range(0,10,1):
    print(i)

# while
j = 3
while j < 10: # j 가 10보다 작을때까지
    print("재훈")
    j = j+1 # j가 0이었는데 여기 만날때마다 j = j+1
if j == 8:
    print("j는 10이야")
else :
    print("j는 값을 모르겠노")

# 변수
jh = "재훈"
print(jh)
a = "재범"
# if else문
if a == jh :
    print("재훈입니다.")
elif a == "재웅":
    print("재웅입니다.")
elif a == "영준":
    print("영준입니다.")
else :
    print("재범입니다.")

# 리스트 (고등학교 한 반)
a = 1
b = 3
c = ["재훈", "재범", "재웅"] # 리스트
print(c)
c.append("연정")
print(c)
c.pop()
print(c)

#함수(function)
# 프로그래밍 하면서 코드 길이가 길어지는 것을 방지
# 더하기 함수  # 매개변수
def fun1(s,w):
    a = fun2(10)
    return s + w + a

def fun2(a):
    return a

c = fun1(10, 5)
print(c)


a = 10
b = 5
c = '재훈'

print(a + b, c)

#a = input()
#b = int(input())
#print("입력받은 값은 " + a + " 입니다.")
#print("입력받은 값은 " , b , " 입니다.")
#print("재훈" + "재훈")

c = ["재훈", "재범", "재웅"] # 리스트
for i in c:
    print(i)

for i in range(10):
    print(i)