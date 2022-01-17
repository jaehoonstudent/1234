## 5장부터 모든 문제는 함수로 작성되어야 합니다.


# 모든 함수를 여러분이 완성하세요.

def pay(rate, hours):
    
    if hours < 40:
        salary = rate * hours
        return salary
    salary = rate * 40
    if hours < 60:
        salary += rate * 1.5 * (hours - 40)
        return salary
    salary += rate * 1.5 * (60 - 40) #20
    salary += rate * 2.0 * (hours - 60)
    return salary

def case(s):
    if s[0].isupper():
        return 'capitalized'
    if s[0].islower():
        return 'not capitalized'
    return 'Unknown'
    

def rps(p1, p2):
    if p1 == p2: return 0
    if p1 == 'R' and p2 == 'P': return 1
    if p1 == 'R' and p2 == 'S': return -1
    if p1 == 'P' and p2 == 'R': return -1
    if p1 == 'P' and p2 == 'S': return 1
    if p1 == 'S' and p2 == 'R': return 1
    if p1 == 'S' and p2 == 'P': return -1

def letter2number(grade):
    if grade[0] == 'A': score = 4.0
    elif grade[0] == 'B': score = 3.0
    elif grade[0] == 'C': score = 2.0
    elif grade[0] == 'D': score = 1.0
    else: score = 0.0
    if len(grade) < 2: return score
    if grade[1] == '+': return score + 0.3
    elif grade[1] == '-': return score - 0.3
    return score

def lastfirst(names):
    last = []
    first = []
    for name in names:
        f, l = name.split(',')
        last.append(l.strip())
        first.append(f.strip())
    return [last, first]


def subsetSum(numbers, target):
    length = len(numbers)
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    return True
    return False

def primes(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False  # 짝수
    for x in range(3, int(n/2)+1, 2):
        if n % x == 0: return False
    return True

def exclamation(word):
    new = ""
    for ch in word:
        if ch in 'aeiou':
            new += ch*4
        else:
            new += ch
    return new+'!'

def primeFact(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)
    return factors 


def encrypt(key, number):
    res = ''
    for c in number:
        res = res + key[int(c)]
    return res

def sublist(lst1, lst2):
    index1 = 0
    index2 = 0

    while index1 < len(lst1):
        while index2 < len(lst2) and lst1[index1] != lst2[index2]:
            index2+=1
        if index2 == len(lst2):
            return False
        index1 += 1
    return True


if __name__ == '__main__':
    # 5.23
    print(pay(10, 35))
    print(pay(10, 45))
    print(pay(10, 61))

    # 5. 24
    print(case('Android'))
    print(case('3M'))
    

    # 5.26
    print(rps('R', 'P'))
    print(rps('R', 'S'))
    print(rps('S', 'S'))

    # 5.27
    print(letter2number('A-'))
    print(letter2number('B+'))
    print(letter2number('D'))

    # 5.29
    names = ['Gerber, Len', 'Fox, Kate', 'Dunn, Bob'] 
    print(lastfirst(names))

    # 5.31
    print(subsetSum([5, 4, 10, 20, 15, 19], 38))
    print(subsetSum([5, 4, 10, 20, 15, 19], 10))

    # 5.36
    print(primes(2))
    print(primes(17))
    print(primes(21))
    
    # 5.39
    print(exclamation('argh'))
    print(exclamation('hello'))

    # 5.42
    print(primeFact(5))
    print(primeFact(72))

    # 5.44
    print(encrypt('3941068257', '132'))
    print(encrypt('3941068257', '111'))

    # 5.48
    print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
    print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))


    

    




