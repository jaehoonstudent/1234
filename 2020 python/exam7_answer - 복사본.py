
# 모든 함수를 여러분이 완성하세요.
# 스스로 풀 수 없는 문제는 main 프로그램에서 지우세요.
import sys
import string
from string import punctuation
import random

def get_words(line):
    ''' 특수 기호를 모두 공백문자로 바꾸로 단어를 반환한다.'''
    # 소문자로 변환한다.
    line = line.strip().lower() 
    # 특수 기호를 모두 공백문자로 바꾼다.
    table = line.maketrans(punctuation, " "*len(punctuation))
    line = line.translate(table)
    # 공백 단위로 단어를 분리한다.
    words = line.split()
    return words
    

def index(file, words):
    ''' 단어들이 사용된 행 수를 반환한다.'''
    lines = dict()
    try:
        fin = open(file)
    except:
        print("File '{}' not found".format(file), file=sys.stderr)
        return lines

    for no, line in enumerate(fin):
        for w in get_words(line):
            if w not in words: continue
            # 사전의 값이 list로 되어 있음.
            if w in lines:
                lines[w].append(no+1)
            else:
                lines[w] = [no+1]
    fin.close()
    return lines
            
                
def game(n):
    count = 0
    for _ in range(n):
        # 두 수를 난수발생기로 생성한다. 
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        print("{} + {} = ".format(x, y))
        
        while True:
            try: 
                ans = int(input("Enter answer : "))
                break
            except:
                print("Please write your answer using 0 through 9. Try again!") 
            
        if ans == x + y:
            print("Correct.")
            count += 1
        else:
            print("Incorrect.")
    return count
            

def inValues():
    count_errors = 0
    total = 0.0
    while count_errors < 2:
        try:
            value = float(input("Please enter a number:"))
            if value == 0.0:
                return total
            total += value
            count_errors = 0
        except:
            count_errors += 1
            print("Error. Please re-enter the value", file=sys.stderr)
    else:
        print("Two errors in a row. Quitting ...")
    return 0.0
    

def reverse1(phonebook):
    rphonebook = dict()
    for k, v in phonebook.items():
        rphonebook[v] = k
    return rphonebook

def reverse(phonebook):
    return {v:k for k, v in phonebook.items()}


def different(table):
    unique_numbers = set()
    for row in table:
        for n in row:
            unique_numbers.add(n)
    return len(unique_numbers)

def simul(n):
    player1, player2 = 0, 0
    # 1 -> 가위, 2 -> 바위, 3 -> 보
    winner = {(1 ,1): 0, (2, 2): 0, (3, 3): 0,
              (1, 2): 1, (1, 3): -1,
              (2, 1): -1, (2, 3): 1,
              (3, 1): 1, (3, 2): -1}
    for _ in range(n):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if winner[(x, y)] == -1:
            player1 += 1
        elif winner[(x, y)] == 1:
            player2 += 1
    if player1 == player2:
        return 'Tie'
    elif player1 > player2:
        return 'Player1'
    else:
        return 'Player2'
        
    
    
if __name__ == '__main__':
    # 7.16
    index_dict = index('raven.txt', ['raven', 'mortal', 'dying', 'ghost', 'ghastly', 'evil', 'demon'])
    for w, line_nos in index_dict.items():
        print(w, end = " ")
        print(*line_nos, sep=', ') # *list는 list unpack에 관련된 내용입니다. 
        


    # 7.17
    n = 3
    count = game(n)
    print("You got {} correct answers out of {}".format(count, n))

    # 7.19
    # 정상적으로 수행
    print(inValues())
    # 비정상적으로 수행
    print(inValues())

    # 6.20
    phonebook = {
        'Smith, Jane': '123-45-67',
        'Doe, John': '987-65-43',
        'Baker, David': '567-89-01'}
    rphonebook = reverse(phonebook)
    for k, v in rphonebook.items():
        print('{} : {}'.format(k, v))

    # 6.25
    print(different([[1,0,1],[0,1,0]]))
    print(different([[1,2,4,5,6],[1, 3, 5, 7, 9, 10], [0,1, 2, 12, 13, 14]]))

    # 6.30
    # simul() 함수의 반환값은 문자열입니다. 
    print(simul(1)) # 난수를 사용하므로 교재의 답과 다를 수 있음
    print(simul(100))



    

    




