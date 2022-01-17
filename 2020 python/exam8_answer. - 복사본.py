
# 모든 함수를 여러분이 완성하세요.
# 스스로 풀 수 없는 문제는 main 프로그램에서 지우세요.
import sys
import string
from string import punctuation
import random
from time import localtime

#Problem 8.20
class BankAccount(object):
    'a bank account class'

    def __init__(self, initial=0):
        'constructor'
        self.b = initial

    def withdraw(self, amount):
        'withdraws amount'
        self.b -= amount

    def deposit(self,amount):
        'deposits amount'
        self.b += amount

    def balance(self):
        'returns balance'
        return self.b
        
#Problem 8.22
class Worker(object):
    'worker class'
    def __init__(self, name, rate):
        'constructs worker object with associated name and pay rate'
        self.name = name
        self.rate = rate

    def changeRate(self, newRate):
        'changes worker rate'
        self.rate = newRate

    def pay(self,hours):
        'returns worker pay'
        print('Not implemented')
        return

class HourlyWorker(Worker):
    'hourly worker class'

    def pay(self, hours):
        'returns hourly worker pay'
        if hours > 40:
            return 40*self.rate + (hours-40)*2*self.rate
        else:
            return hours*self.rate

class SalariedWorker(Worker):
    'salaried work class'

    def pay(self, hours=None):
        'returns salaried worker pay'
        return 40*self.rate


#Problem 8.24
class Person(object):
    'person class'

    def __init__(self, name, birthYear):
        'constructs person with given name and birth year'
        self.personName = name
        self.birthYear = birthYear

    def age(self):
        'computes and returns person age'
        return localtime()[0] - self.birthYear

    def name(self):
        'returns person name'
        return self.personName

# Problem 8.29
class Hand(object):
    'represents a hand of playing cards'

    def __init__(self, player):
        'initializes player ID and initial empty hand'
        self.player = player
        self.hand = []

    def addCard(self, card):
        'adds card to hand'
        self.hand.append(card)

    def showHand(self):
        'prints player ID and hand'
        print('{}:'.format(self.player), end='')
        for card in self.hand:
            rank = card.getRank()
            suit = card.getSuit()
            print('{:>4} {}'.format(rank, suit), end = '')
        print()
        return
    
class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)

# Problem 8.33
class Pseudorandom(object):
    'linear congruential pseudorandom number generator'

    def __init__(self, seed, multiplier, increment, modulus):
        '''contructs a generator with given seed, multiplier,
           increment, and modulus'''
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus

    def next(self):
        'returns next pseudorandom number'
        self.seed = (self.multiplier*self.seed+self.increment)%self.modulus
        return self.seed

# Problem 8.36
class PriorityQueue(object):
    'Priority queue class'

    def __init__(self):
        'constructor initializes empty priority queue'
        self.l = []

    def insert(self, item):
        'inserts item into priority queue'
        self.l.append(item)
        self.l.sort(reverse=True)

    def min(self):
        'returns minimum item in priority queue'
        return self.l[-1]

    def removeMin(self):
        'removes minimum item in priority queue'
        self.l.pop()

    def __len__(self):
        'returns size of priority queue'
        return len(self.l)

    def isEmpty(self):
        'checks whether priority queue is empty'
        return len(self) == 0

# Problem 8.39
class Animal(object):
    'animal class'
    def speak(self):
        print('')

class Mammal(Animal):
    'mammal class'
    def speak(self):
        print('Mama!')

class Cat(Mammal):
    'cat class'
    def speak(self):
        print('Meeow!')

class Dog(Mammal):
    'dog class'
    def speak(self):
        print('Wooof!')

class Primate(Mammal):
    'primate class'
    def speak(self):
        print('Boooh')

class Hacker(Primate):
    'hacker class'
    def speak(self):
        print('Hello World!')


if __name__ == '__main__':
    # 8.20
    x = BankAccount(700)
    print(x.balance())
    x.withdraw(70)
    print(x.balance())
    x.deposit(7)
    print(x.balance())

    # 8.22
    w1 = Worker('Joe', 15)
    print(w1.pay(35))
    w2 = SalariedWorker('Sue', 14.50)
    print(w2.pay())
    print(w2.pay(60))
    w3 = HourlyWorker('Dana', 20)
    print(w3.pay(25))
    w3.changeRate(35)
    print(w3.pay(25))

    # 8.24
    p1 = Person('Smith', 2000)
    print(p1.age())
    print(p1.name())

    # 8.29
    hand = Hand('House')
    deck = Deck()
    deck.shuffle()
    hand.addCard(deck.dealCard())
    hand.addCard(deck.dealCard())
    hand.addCard(deck.dealCard())
    print(hand.showHand())

    # 8.33
    x = Pseudorandom(17, 12, 7, 31)
    print(x.next())
    print(x.next())
    print(x.next())

    # 8.36
    p = PriorityQueue()
    p.insert(3)
    p.insert(1)
    p.insert(5)
    p.insert(2)
    print(p.min())
    p.removeMin()
    print(p.min())
    print(len(p))
    print(p.isEmpty())

    # 8.39
    garfield = Cat()
    print(garfield.speak())
    dude = Hacker()
    print(dude.speak())
    
    
    


    
    


    

    




