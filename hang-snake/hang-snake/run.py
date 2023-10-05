from common.util import clear_terminal
import random


def create_secret():
    f = open('word.txt', 'r')
    mas = f.readlines()
    f.close()
    return random.choice(mas).strip()


def string(a):
    SIMBOLS_LUCKY.append(a)
    st = ""

    for i in SECRET:
        if i in SIMBOLS_LUCKY:
            st += str(i)
        else:
            st += "."

    return st
    

SECRET = create_secret()

SIMBOLS_UNICAL = []
SIMBOLS_LUCKY = []
for i in SECRET:
    if i not in SIMBOLS_UNICAL:
        SIMBOLS_UNICAL.append(i)

k = len(SECRET)


FIELD_START = r'''
'''

FIELD_2 = r'''
        +
        |
        |
        |
        |
_______/|\_
'''

FIELD_3 = r'''
   +----+
        |
        |
        |
        |
_______/|\_
'''

FIELD_4 = r'''
   +----+
   |    |
        |
        |
       |
_______/|\_
'''

FIELD_5 = r'''
   +----+
   |    |
   o    |
        |
        |
_______/|\_
'''

FIELD_6 = r'''
   +----+
   |    |
   o    |
   |    |
        |
_______/|\_
'''

FIELD_7 = r'''
   +----+
   |    |
   o    |
   |\   |
        |
_______/|\_
'''

FIELD_8 = r'''
   +----+
   |    |
   o    |
  /|\   |
        |
_______/|\_
'''

FIELD_9 = r'''
   +----+
   |    |
   o    |
  /|\   |
    \   |
_______/|\_
'''

FIELD_FINAL = r'''
   +----+
   |    |
   o    |
  /|\   |
  / \   |
_______/|\_
'''


Field = [FIELD_START, FIELD_2, FIELD_3, FIELD_4, FIELD_5,
     FIELD_6, FIELD_7, FIELD_8, FIELD_9, FIELD_FINAL]
FIELD = FIELD_START
n = 0
f = True

while f:
    letter = input('Enter your guess: ')

    while len(letter) != 1:
        letter = input('Enter your guess: ')
    
    if letter not in SECRET:
        
        n = n + 1
        FIELD = Field[n]
        st = string(letter)
        print(st)
        if FIELD == FIELD_FINAL:
           f = False
    else:
        st = string(letter)
        print(st)
        if st == SECRET:
            f = False
        

    clear_terminal()
    print(FIELD)
