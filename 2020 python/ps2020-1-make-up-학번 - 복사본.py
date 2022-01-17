import math
import string
import random

    
if __name__ == '__main__':
    # 0
    name = '이름'     # '이름'을 본인의 이름으로 수정하세요.
    id_no = '학번'    # '학번'을 본인의 학번으로 수정하세요.
    print(name, id_no)

    # 풀 수 없는 문제는 주석으로 처리하세요.
    
    # 1
    print('1. {}'.format( volume(30) ))
    
    # 2
    print('2. {}'.format( coin(0.000001) ))

    # 3
    print('3. {}'.format( valid_float() ))

    #4 
    print('4. {}'.format( month(3) ))

    #5
    print('5. {}'.format( nFibonacci(10) ))

    #6
    print('6. {}'.format( compute_pi(200000) ))

    #7
    print('7. {}'.format( exchange_case("Computer Science") ))

    #8
    print('7. ')
    statistics = characteristics('novel.txt')
    print('총 단어 수         : ', statistics[0])
    print('총 줄 수           : ', statistics[1])
    print('단어의 평균 문자 수: ', statistics[2])
    print('줄 당 평균 단어 수 : ', statistics[3]) 

    #9
    words = possible('novel.txt')
    top10 = [w for w in words if w[0].isalpha() and w[1].isalpha()][:10]
    print(top10)

##    # 수고하셨습니다.
##    # 좋은 결과가 있기를 기원합니다. 
