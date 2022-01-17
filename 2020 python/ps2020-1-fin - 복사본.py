import re
import math


#1
def recSum(lst):
    return sum(lst)
# 화살표 뒤의 내용은 반환값의 자료형입니다.
    #완성하시오.


#2     
def silly(n):
    if n=0:
        return 0
    return [*]+silly(n-1)+[!]


#3
def reverse(n) -> int:
    #완성하시오.

#4
def median(lst) -> float:
    #완성하시오.

#5
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(dx, dy):
        self.x += x
        self.y += y

    #완성하시오.
    
#6
class Segment:
    #완성하시오.
        
#7
def get_prefix(file, prefix) -> set:
    #완성하시오.  

if __name__ == '__main__':
    # 0
    name = '이름'     # '이름'을 본인의 이름으로 수정하세요.
    id_no = '학번'    # '학번'을 본인의 학번으로 수정하세요.
    print(name, id_no)

    # 풀 수 없는 문제는 주석으로 처리하세요.
    #1
    no = 1
    print('------{}번'.format(no))
    print(recSum([1, 2, 3, 4, 5]))
    
    #2
    no += 1
    print('------{}번'.format(no))
    print(''.join(silly(1)))
    print(''.join(silly(10)))

    #3
    no += 1
    print('------{}번'.format(no))
    print(reverse(1234))
    
    #4
    no += 1
    print('------{}번'.format(no))
    print(median([1, 2, 100]))
    print(median([1, 10, 90, 100]))

    #5
    no += 1
    print('------{}번'.format(no))
    p1 = Point(1, 2)
    print(p1)
    p2 = Point(2, 3)
    print(p1 + p2)
    print(p1 - p2)
    print(p1 < p2)
    print(p1 == p2)
    print(p1 != p2)

    #6
    no += 1
    print('------{}번'.format(no))
    p1 = Point(3, 4)
    p2 = Point()
    s = Segment(p1, p2)
    print(s)
    print(s.length())
    print(s.slope())
    print(s.degree())
    
    
    #7
    no += 1
    print('------{}번'.format(no))
    words = get_prefix('novel.txt', '한화')
    print(len(words), sorted(words))
    

    # 수고하셨습니다.
    # 좋은 결과가 있기를 기원합니다.
    
