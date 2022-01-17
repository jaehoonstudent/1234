 
# 모든 함수를 여러분이 완성하세요.
# 스스로 풀 수 없는 문제는 main 프로그램에서 지우세요.
import sys
import string
from string import punctuation
import random
from time import localtime
from os import listdir
from os.path import join

# Problem 10.16
def combinations(n, k):
    'returns the number of ways of choosing k items out of n'
    if k==0:
        return 1
    elif n < k:
        return 0
    else:
        return combinations(n-1,k-1)+combinations(n-1,k)


# Problem 10.20
def rgcd(a, b):
    'returns the greatest common denominator of non-negative integers a and b'
    if b == 0:
        return a
    return rgcd(b, a%b)

# Problem 10.21
def rem(lst):
    'returns copy of list lst in which one copy of every duplicate item is removed'
    # sort list first so duplicates are adjacent
    lst.sort()
    new=[]

    # an item of lst is added to list new only if it is equal to
    # the item preceding it
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            new.append(lst[i])
    return new

# Problem 10.24
def base(n, b):
    'returns base-b (1 < b < 10) representation of non-negative integer n'
    if n < b:
        return str(n)
    else:
        return base(n//b, b) + str(n%b)

# Problem 10.25
def permutations(lst):
    'returns list of all permutations (represented as lists) of list lst'
    if len(lst) < 2:
        return [lst]
    perms = permutations(lst[1:])

    res = []
    for perm in perms:
        for i in range(len(lst)):
             res.append(perm[:i] + [lst[0]] + perm[i:])
    return res

# Problem 10.26
def strPermutations(s):
    'returns list of all permutations of characters of string s'
    if len(s) < 2:
        return [s]
    perms = strPermutations(s[1:])
    res = []
    for perm in perms:
        for i in range(len(s)):
             res.append(perm[:i]+s[0]+perm[i:])
    return res

def anagrams(filename, word):
    'prints anagrams of word based on words in file filename'
    infile= open(filename)
    wordList = infile.read().split()
    infile.close()
    perms = strPermutations(word)
    return [perm for perm in perms if perm in wordList]

# Problem 10.27
def pairs1(lst, target):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return True
    return False
               

def pairs2(lst, target):
    lst.sort()
    i = 0            # index of smaller integer in pair
    j = len(lst)-1   # index of larger integer in pair
    while i < j:
        s = lst[i] + lst[j] 
        if s == target:
            return True
        elif s < target: # sum is too small, so consider next smallest integer 
            i+=1
        else:            # sum is too large, so consider next largest integer
            j-=1
    return False

    

# Problem 10.29
def pascalLine(n):
    '''returns a list containing the sequence of numbers appearing in the
       nth line of Pascal’s triangle'''
    if n == 0:       # base case
        return [1]

    # induction step: start by generating line n-1
    prev = pascalLine(n-1)

    # use line n-1 to generate line n
    res = [1]
    for index in range(len(prev)-1):
        res.append(prev[index]+prev[index+1])
    res.append(1)
    return res

# Problem 10.30

def traverse(path, depth):
    '''Prints the relative pathname of every file and subfolder contained,
       directly or indirectly, in the folder described by pathname path.
       
       Integer depth specifies the indentation to be used when printing.'''
    for item in listdir(path):
        itemPath = join(path, item)
        print(' '*2*depth+itemPath)
        try:    # recursively traverse a subfolder
            traverse(itemPath, depth+1)
        except: # base case: exception means that item is a file
              pass

# Problem 10.34
def recDup(lst):
    'returns a copy of list lst in which every item has been duplicated'
    if len(lst) == 0:
        return []
    return recDup(lst[:-1]) + [lst[-1]]*2

# Problem 10.35
def recReverse(lst):
    'returns a reversed copy of list lst'
    if len(lst) == 0:
        return []
    return [lst[-1]] + recReverse(lst[:-1])

# Problem 10.36
def recSplit(lst, i):
    if i == 0:
        return [lst, []]
    res = recSplit(lst[:-1], i-1)
    return [res[0], res[1]+[lst[-1]]]


if __name__ == '__main__':
    # 10.16
    print(combinations(1, 2))
    print(combinations(2, 1))
    print(combinations(5, 2))

    # 10.20
    print(rgcd(3, 0))
    print(rgcd(18, 12))

    # 10.21
    print(rem([4]))
    print(rem([4, 4]))
    print(rem([4, 1, 3, 2]))
    print(rem([2, 4, 2, 4, 4]))

    # 10.21
    print(base(0, 2))
    print(base(1, 2))
    print(base(10, 2))
    print(base(10, 3))

    # 10.25
    print(permutations([1, 2]))
    print(permutations([1, 2, 3]))
    print(permutations([1, 2, 3, 4]))

    # 10.26
    print(anagrams('words.txt', 'trace'))

    # 10.27
    # skip the timeingAnalysis
    print(pairs1([4, 1, 9, 3, 5], 13))
    print(pairs1([4, 1, 9, 3, 5], 11))

    print(pairs2([4, 1, 9, 3, 5], 13))
    print(pairs2([4, 1, 9, 3, 5], 11)) 

    # 10.29
    print(pascalLine(0))
    print(pascalLine(2))
    print(pascalLine(3))
    print(pascalLine(4))

    # 10.30
    traverse('test', 0)

    # 10.34
    print(recDup(['ant', 'bat', 'cat', 'dog']))

    # 10.35
    lst = [1, 3, 5, 7, 9]
    print(recReverse(lst))

    # 10.36
    print(recSplit([1, 2, 3, 4, 5, 6, 7], 3))
    print(recSplit([1, 2, 3, 4, 5, 6, 7], 5))
    
    
    

    
    
    

    
    
    


    
    


    

    




