print('조재훈')#print문
print('조재훈','조재범')
print('조재훈'+'조재범')
print(22)
a='조재훈'
print(a)
a=22
print(a)
"""이건 줄관계없이 주석을 달고싶을떄 써
다음줄에도 상관없는거 확인ㅇ"""
#연산자
a=3
b=5
plus=a+b
minus=a-b
multiply=a*b
division=a/b
reminder=a%b
power=a**b#a의 b승
quotient=a//b #a와 b 나눌떄 몫만 나옴
print(plus,minus,multiply,division,reminder,power,quotient)
#if문
a=3
b=4
if a>b:
    print('{}보다 {}가 크다.'.format(b,a))
elif a<b:
    print('{}보다 {}가 작다.'.format(b,a))
else:
    print('{}와 {}가 같다')
"""조건식 
숫자비교
크다 < 
크거나 같다 < = 
같다 ==
같지않다 ! = 
비교 결과는 True,False
and: 20<=a and a<30 and는 두조건이 모두 참이면 true
or: a<18 or 60< = a or는 두조건중 하라라도 참이면 true
not: ! """
if True:
    print("if문 조건식에 true가 적히면 프린트가 된다")
if False:
    print('if문 조건식에 False가 적히면 프린트가 안된디')
#사용자 입력받기

#mine=input()
#print('mine:',mine)
#mine=input('가위 바위 보 가운데 하나를 내주세요')
#print('mine:',mine)

list1=[1,2,3,4,5]
print(list1[0])#값 읽어오기 list1[0]
list1[0]=10 #리스트수정
print(list1[0])
# 리스트에 값을 추가하는 방법
list1.append(6)
print(list1)

list2=list1+[7]
print(list2)

del list1[5] #인덱스를 지정해서 값을 지울떄 써
print(list1)

list1.remove(5)  #값을 바로 지울떄 써
print(list1)

#리스트안에 값이 있는지 찾을떄 사용
n=3
if n in list1:
    print('{}가 리스트에 있다.'.format(n))

list3=[1,2,3,4,5,6]
list4=[7,8,9,10,11,12]
print(list3+list4)

for a in list3:
    print(a)

for i in range(4):#0.1.2.3
    print(i)

for i in range(1,6,2):#스타트인덱스,스탑인덱스,더하기몇
    value=list3[i]
    print('{}번: {}.'.format(i+1,value))

for i,value in enumerate(list4):
    print('{}번: {}'.format(i+1,value))

#함수만들기
def fun(s,w):
    return s*w
c=fun(3,4)
print(c)

import datetime
print(datetime.date.today())
import random
list=['빨','주','노','초','파','남','보']
random_element=random.choice(list)
print(random_element)

#딕셔너리
simple={
    1:'a',
    2:'b',
    3:'c',
}
print(simple[2])



