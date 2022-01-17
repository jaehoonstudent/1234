import string

## 6장부터 모든 문제는 함수로 작성되어야 합니다.


# 모든 함수를 여러분이 완성하세요.
# 스스로 풀 수 없는 문제는 main 프로그램에서 지우세요.

def ticker(fname):
    text = open(fname).read()
    text = text.strip()
    lines = text.split('\n')
    companys = lines[0::2]
    tickers = lines[1::2]
    return {k.strip():v.strip() for k, v in zip(companys, tickers)}   

def mirror(word):
    mirror_images = {
        'a':'', 'b':'d', 'c':'', 'd':'b', 'e':'', 'f':'', 'g':'',
        'h':'', 'i':'i', 'j':'', 'k':'', 'l':'l', 'm':'m', 'n': 'n',
        'o':'o', 'p':'q', 'q':'p', 'r':'', 's':'', 't':'',
        'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'', 'z':''}
    mirror_word = ''
    for ch in word:
        mirror_word = mirror_images[ch] + mirror_word
    return mirror_word if len(word) == len(mirror_word) else 'INVALID'
                    
def scaryDict(fname):
    text = open(fname).read()
    special = string.punctuation
    table = text.maketrans(special, ' '*len(special))
    text = text.translate(table)
    text = text.lower()
    words = text.split()
    return {w for w in words if len(w) > 2}

def write_words(scary_words, fname):
    ofile = open(fname, 'w')
    for w in sorted(scary_words):
        print(w, file=ofile)

def index(fname, keys):
    indexes = {k : [] for k in keys}
    special = string.punctuation
    for i, line in enumerate(open(fname)):
        line = line.strip().lower()
        table = line.maketrans(special, ' '*len(special))
        line = line.translate(table)
        words = line.split()
        for w in words:
            if w in indexes:
                indexes[w].append(i+1)
    return indexes

def networks(n, friendsList):
    sets = [{i} for i in range(n)]
    for x, y in friendsList:
        union = set()
        i = 0
        while i < len(sets):
            if (x in sets[i]) or (y in sets[i]):
                union |= sets[i]
                sets.pop(i)
            else:
                i += 1
        sets.append(union)
    return sets


def zipf(fname):
    text = open(fname).read()
    special = string.punctuation
    table = text.maketrans(special, ' '*len(special))
    text = text.translate(table)
    text = text.lower()
    words = text.split()
    freq = dict()
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
    
def caesar(n, fname):
    text = open(fname).read()
    crypt = []
    for ch in text:
        if ch in string.ascii_lowercase:
            ch = chr(ord('a') + (ord(ch) - ord('a') + n) % 26)
        elif ch in string.ascii_uppercase:
            ch = chr(ord('A') + (ord(ch) - ord('A') + n) % 26)
        crypt.append(ch)
    return ''.join(crypt)
            
def write_crypt(crypt, fname):
    ofile = open(fname, 'w')
    print(crypt, file=ofile, end='')
    ofile.close() 


    
if __name__ == '__main__':
    # 6.21
    # 사전 {회사명: 주식종목명}를 반환한다.
    ticker_symbols = ticker('nasdaq.txt')
    for i in range(2):
        company = input("Enter Company name :")
        if company in ticker_symbols:
            print("Ticker symbol : {}".format(ticker_symbols[company]))
        else:
            print("Wrong Company")

    # 6.22
    print(mirror('vow'))
    print(mirror('wood'))
    print(mirror('bed'))

    # 6.23
    # 문제에서 기술대로 단어를 구해서 word set을 반환한다.
    scary_words = scaryDict('frankenstein.txt') 
    # word set을 'dictionary.txt'에 저장한다.
    # 책에서 출력된 것처럼 정렬된 형식으로 저장되어야 한다. 
    write_words(scary_words, 'dictionary.txt')  
    
    # 6.27
    index_dict = index('raven.txt', ['raven', 'mortal', 'dying', 'ghost', 'ghastly', 'evil', 'demon'])
    # key: str인 단어
    # value: list인 행 번호들 
    for k, v in index_dict.items():
        print(k, *v, sep=', ') # *v를 list에서 [ ]를 제거하는(unpack) 연산자이다.  

    # 6.29
    friends_sets = networks(5, [(0, 1), (1, 2), (3, 4)])
    for i, s in enumerate(friends_sets):
        print('Social networks {} is {}'.format(i, s))

    # 6.36
    crypt = caesar(3, 'clear.txt')
    write_crypt(crypt, 'cipher.txt')  

    # 6.37
    freq = zipf('frankenstein.txt')
    N = sum(freq.values())
    most_frequent = sorted(freq, key=freq.get, reverse=True)
    most_frequent = most_frequent[:10]
    for k, w in enumerate(most_frequent):
        print(freq[w]/N * (k+1))



    

    




