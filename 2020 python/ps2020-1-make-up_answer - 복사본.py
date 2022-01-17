import math
import string
import random
import sys

#1
def volume(r):
    return 4/3 * math.pi * pow(r, 3.0) #r ** 3
#2
def coin(err):
    n = 0
    head = 0
    while True:
        head += random.randint(0,1)
        n += 1
        pr_of_head = head / n
        pr_of_tail = 1.0 - pr_of_head
        if math.fabs(pr_of_head - pr_of_tail) < err:
            break
    return n

#2-1
def coin(err):
    n_head, n = 0.0
    phead, ptail = 1.0, 0.0
    while math.fabs(phead - ptail) > err:
        n_head += random.randint(0,1) #0:tail, 1:head
        n += 1
        phead = n_head / n
        ptail = 1.0 - phead
    return n

#3
def valid_float():
    while True:
        value = input("실수를 입력하시오:")
        try:
            value = float(value)
            return value
        except:
            print("입력 값 '{}'을 실수가 아닙니다.".format(value), file=sys.stderr)
            print("다시 입력하시오", file=sys.stderr)

#4 list   
def month(m):
    korean=['해오름', '시샘', '물오름', '잎새', '푸른', '누리',
            '견우직녀', '타오름', '열매', '하늘연', '마름', '매듭']
    return korean[m-1] + '달'
#4-1 dic
def month(m):
    korean={1:'해오름', 2:'시샘', 3:'물오름', 4:'잎새', 5:'푸른', 6:'누리',
            7:'견우직녀',8: '타오름', 9:'열매', 10:'하늘연', 11:'마름', 12:'매듭'}
    return korean[m] + '달'

#5
def nFibonacci(n):
    f0 = 1
    f1 = 1
    if n == 0: return 1
    if n == 1: return 2
    count = 2
    while f1 <= n:
        f0, f1 = f1, f0 + f1
        count += 1
    else:
        count -= 1
    return count

#6
def compute_pi(n):
    pi = 0
    for i in range(0, n):
        numerator = (i*2 + 1) * (-1 if i % 2 else 1)
        pi += 4 / numerator
    return pi

#6-1
def compute_pi(n):
    pi = 0
    for i in range(n):
        if i % 2 == 0:
            pi += 4 / (i*2 + 1) # 0->1, 1->3, 2->5, 3->7
        else:
            pi -= 4 / (i*2 + 1)
    return pi

#6-2
def compute_pi(n):
    pi = 0
    for i in range(n):
##        fact = 1 if i % 2 == 0 else -1
        pi += (1 if i % 2 == 0 else -1) * 4 / (i*2 + 1)
    return pi

#6-3 
def compute_pi(n):
    return sum([(1 if i % 2 == 0 else -1) * 4 / (i*2 + 1) for i in range(n)])


#7
def exchange_case(word):
    return word.swapcase()
#7-1
def exchange_case(s):
    res = ''
    for ch in s:
        if ch.islower():
            res += ch.upper()
        elif ch.isupper():
            res += ch.lower()
        else:
                res += ch
    return res


#8
def characteristics(file):
    no_lines = 0
    no_words = 0
    len_words = 0
    symbols = string.punctuation
    for line in open(file):
        #특수문자를 모두 공백으로 변환 
        table = line.maketrans(symbols, " "*len(symbols))
        line = line.translate(table)
        #공백 단위의 단어 리스트를 구한다.
        words = line.split()
        
        if len(words) <= 0: continue
        #통계치 집계 
        no_lines += 1
        no_words += len(words)
        len_words += sum([len(w) for w in words])
    return no_words, no_lines, len_words / no_words, no_words / no_lines

#9   
def possible(file):
    text = open(file).read()
    #문자의 빈도수를 센다.
    fc = dict()
    for c in text:
        fc[c] = fc.get(c, 0) + 1
    #bigram의 빈도수를 센다.
    fw = dict()
    for c1, c2 in zip(text, text[1:]):
        bigram = c1 + c2
        fw[bigram] = fw.get(bigram, 0) + 1

    N = len(text)
    dwords = dict()
    for w in sorted(fw, key=fw.get, reverse=True):
        pr_w = fw[w] / N
        pr_c1 = fc[w[0]] / N
        pr_c2 = fc[w[1]] / N

        score = math.log(pr_w / (pr_c1 * pr_c2))
        if score > 0.0:
            dwords[w] = score
    return sorted(dwords, key=dwords.get, reverse=True)

    
if __name__ == '__main__':
    # 0
    name = '이름'     # '이름'을 본인의 이름으로 수정하세요.
    id_no = '학번'    # '학번'을 본인의 학번으로 수정하세요.
    print(name, id_no)

    # 풀 수 없는 문제는 해당 호출문을 주석으로 처리하세요.

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
    statistics = characteristics('novel.txt')
    print('총 단어 수         : ', statistics[0])
    print('총 줄 수           : ', statistics[1])
    print('단어의 평균 문자 수: ', statistics[2])
    print('줄 당 평균 단어 수 : ', statistics[3]) 

    #9
    words = possible('novel.txt')
    top10 = [w for w in words if w[0].isalpha() and w[1].isalpha()][:10]
    print(top10)


####    # 수고하셨습니다.
####    # 좋은 결과가 있기를 기원합니다.
####    
