# 12월 29일
class Car():
    '''자동차'''

    def run(self): # run메소드 정의
        print("{}가 달립니다.".format(self.name))

    def back(self): # 메소드 정의
        print("{}가 후진합니다.".format(self.name))


jb = Car() # 자동차의 한 종류 jb ==>> 인스턴스
jb.name = "재범이"
print(jb.name + "는 자동차 이름입니다.")
jb.run()
jh = Car()
yj = Car()

taxi = Car()
taxi.name = "택시"
taxi.run()


def walk1():
    print("111걷는다")

class Animal():
    def walk(self):
        print("222걷는다")
class Human(Animal):
    def wave(self):
        print("손을 흔든다")

walk1() # 그냥 walk1()를 호출

bbb = Animal() # 인스턴스 생성
bbb.walk() # walk()를 호출

# 상속 할아버지 - 아빠 - 재훈
class Animal(): # 할아버지
    def walk(self):
        print("걷는다")

class Human(Animal): # 아빠
    def wave(self):
        print("손을 흔든다")

# 인스턴스 생성
aaa = Animal()
aaa.walk()

bbb = Human()
bbb.walk()

# 오버라이드
class Animal( ):
    def greet( self ):
        print( "인사한다" )

class Human( Animal ):
    def greet( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def greet( self ):
        print( "꼬리를 흔든다" )