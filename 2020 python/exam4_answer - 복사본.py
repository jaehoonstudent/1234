## 4장부터 모든 문제는 함수로 작성되어야 합니다.

def month(n):
    # 프로그램을 작성한다.
    return month_name

# 이하는 여러분이 완성하세요.

def month(num):
    abbr =['Jan', 'Feb', 'Mar', 'Apr', 'May',
           'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return abbr[num-1]

def vowelCount(word):
    vcount = [0, 0, 0, 0, 0]
    word = word.lower()
    for ch in word:
        if 'a' in ch: vcount[0] += 1
        if 'e' in ch: vcount[1] += 1
        if 'i' in ch: vcount[2] += 1
        if 'o' in ch: vcount[3] += 1
        if 'u' in ch: vcount[4] += 1
    return vcount


def fcopy(fin, fout):
    intext = open(fin).read()
    outfile = open(fout, 'w')
    outfile.write(intext)
    outfile.close()


def stats(filename):
    ' prints the number of lines, words, and characters in file filename'
    # get file content
    infile = open(filename)
    content = infile.read()
    infile.close()

    # replace punctuation with blank spaces and obtain list of words
    table = str.maketrans('.,;!?:\n', 7*' ' )
    words = content.translate(table).split()

    no_lines = content.count('\n')
    no_words = len(words)
    no_chars = len(content)
    return no_lines, no_words, no_chars

def duplicate(filename):
    content = open(filename).read()

    table = str.maketrans('.,;!?:\n', 7*' ' )
    words = content.translate(table).split()

    for word in words:
        if words.count(word) > 1:
            return True
    return False

           
if __name__ == '__main__':
    # 4.22
    print(month(1))
    print(month(12))

    # 4.25
    vcount = vowelCount('Le Tour de France')
    print('a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times.'.format(
        vcount[0], vcount[1],
        vcount[2], vcount[3],  vcount[4]))

    # 4.27
    ifile = 'example.txt'
    ofile = 'output.txt'
    fcopy(ifile, ofile)
    # 두 파일의 내용이 같아야 한다.
    print(open(ifile).read())
    print(open(ofile).read())

    # 4.29
    lines, words, chars = stats(ifile)
    print('line count : {}'.format(lines))
    print('word count : {}'.format(words))
    print('chararcter count : {}'.format(chars))

    # 4.31
    # 여러분이 파일을 만들어서 사용하세요.
    print(duplicate('Duplicates.txt')) # True or False
    print(duplicate('noDuplicates.txt'))

    





