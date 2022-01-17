import math
import string
import random

# 1
"""def volume(r):
    result=4/3 * math.pi * r*r*r
    return result
# 2
def coin(error):
    n=0
    head=0
    while True:
        head += random.randint(0,1)
        n+=1
        per_head= head/n
        per_down= 1- per_head
        per=abs(per_head-per_down)
        if per<error:
            break
    return n

#  3
def valid_float():
    float=input('실수를 입력하시오')
    while True:
        try:
            value = float(value)
            return value
        except:
            print("입력값'{}'을 실수가 아닙니다".format(value))
            print("다시 입력하시오")

# 4
def month(n):
    list_month=['해오름달','시샘 달','물오름 달','잎새달','푸른 달','누리 달','견우처녀 달','타오름 달','열매 달','하늘 연달','마름 달','매듭 달']
    return list_month[n-1]"""

# 5
def nFibonacci(n):
    list=[1,1]
    k=2

    count=0
    while True:
        new_list= list[k-2]+list[k-1]
        if new_list > n:  # 무한루프를 돌리면 컴퓨터가 감당을 못한다..
            break
        list.append(new_list)
        k+=1
    r=0
    while True:
        if list[r] > n:
            break
        if list[r] <= n:
            count+=1
            r+=1

    return count
        
# 6
"""def compute_pi(n):
    k=1
    while True:
        pi+=4/(k)
        if pi<0:
            k=2-k
        else:
            k=-2-k
    return pi

# 7
def exchange_case(word):
    return word.swapcase()"""








    
if __name__ == '__main__':
    # 0
    name = '이름'     # '이름'을 본인의 이름으로 수정하세요.
    id_no = '학번'    # '학번'을 본인의 학번으로 수정하세요.
    print(name, id_no)

    # 풀 수 없는 문제는 주석으로 처리하세요.
    
    # 1
    #print('1. {}'.format( volume(30) ))
    
    # 2
    #print('2. {}'.format( coin(0.000001) ))

    # 3
    #print('3. {}'.format( valid_float() ))

    #4 
    #print('4. {}'.format( month(3) ))

    #5
    print('5. {}'.format( nFibonacci(10) ))

    #6
    #print('6. {}'.format( compute_pi(200000) ))

    #7
    #print('7. {}'.format( exchange_case("Computer Science") ))

    #8
    #print('7. ')
    #statistics = characteristics('novel.txt')
    #print('총 단어 수         : ', statistics[0])
    #print('총 줄 수           : ', statistics[1])
    #print('단어의 평균 문자 수: ', statistics[2])
    #print('줄 당 평균 단어 수 : ', statistics[3])

    #9
    #words = possible('novel.txt')
    #top10 = [w for w in words if w[0].isalpha() and w[1].isalpha()][:10]
    #print(top10)"""

##    # 수고하셨습니다.
##    # 좋은 결과가 있기를 기원합니다. 
