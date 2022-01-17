import re
import math

#1
def recSum(lst) -> int:
    if len(lst) == 0: return 0
    return lst[0] + recSum(lst[1:]) 

#2     
def silly(n) -> list:
    if n == 0: return []
    return ['*'] + silly(n-1) + ['!']  

#3
def reverse(n) -> int:
    return reverse1(n, 0)

def reverse1(n, m) -> int:
    return m if n == 0 else reverse1(n//10, m *10 + n % 10)

#4
def median(lst) -> float:
    mid = len(lst) // 2;
    return lst[mid] if len(lst) % 2 else  (lst[mid-1] + lst[mid]) / 2 

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

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self == other)
  
    def __str__(self):
        return 'Point({}, {})'.format(self.x, self.y)
    
#6
class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return math.sqrt((p1.getx() - p2.getx())**2 + (p1.gety() - p2.gety())**2)

    def slope(self):
        deltaX = p2.getx() - p1.getx()
        deltaY = p2.gety() - p1.gety()
        return deltaY / deltaX

    def degree(self):
        try:
            theta2 = math.atan(p2.gety() / p2.getx())
        except:
            theta2 = 0
        try:
            theta1 = math.atan(p1.gety() / p1.getx())
        except:
            theta1 = 0
            
        theta = theta2 - theta1
        return theta * 180 / math.pi
    
    def __repr__(self):
        return "Segment({}, {})".format(self.p1, self.p2)
        
#7
def get_prefix(file, prefix):
    text = open(file).read()
    return set(re.findall(prefix+'[가-힝]+', text))    

if __name__ == '__main__':
    # 0
    name = '이름'     # '이름'을 본인의 이름으로 수정하세요.
    id_no = '학번'    # '학번'을 본인의 학번으로 수정하세요.
    print(name, id_no)

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
    
