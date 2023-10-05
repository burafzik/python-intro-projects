from pynput import keyboard
from random import randint
import random
from common.util import clear_terminal
import time

TERM_FLAG = "IDLE"

WIDTH, HEIGHT = 20, 20
direction = [0, 0]


f = True
win = False
snake = []
apple = []
banana = []
strawberry = []
a, b, s = '', '', ''
score = 0


def cls():
    if TERM_FLAG == "IDLE":
        for i in range(HEIGHT * 10):
            print()
    else:
        clear_terminal()
    

def random_position():
    return [randint(1, HEIGHT - 2), randint(1, WIDTH - 2)]


def process_press(key):
    global direction
    if key == keyboard.Key.left:
        direction = [-1, 0]
    elif key == keyboard.Key.up:
        direction = [0, -1]
    elif key == keyboard.Key.right:
        direction = [1, 0]
    elif key == keyboard.Key.down:
        direction = [0, 1]


def new_apple(snake):
    apple = random_position()
    while apple in snake:
        apple = random_position()
    return apple


def new_banana(snake, apple):
    banana = random_position()
    while banana in snake or banana == apple:
        banana = random_position()
    return banana


def new_strawberry(snake, apple, banana):
    strawberry = random_position()
    while strawberry in snake or strawberry == apple or strawberry == banana:
        strawberry = random_position()
    return strawberry


def new_letter(sp, c):
    l = random.choice(sp)
    while l == c:
        l = random.choice(sp)
    return l


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


def show_snake_info():
#    print(snake)
#    print(apple)
#    print(banana)
#    print(strawberry)
#    print(SIMBOLS_UNICAL)
#    print(a, b, s)
    pass


def draw_board(score):
    cls()
    
    print(f"score = {score}")

    print(FIELD)
    print()
    print(st)

    show_snake_info()

    for i in range(WIDTH):
        print("#", end="")

    print()

    for j in range(HEIGHT - 2):
        print("#", end="")
        for i in range(1, WIDTH - 1):
            if [i, j + 1] == apple:
                print(a, end="")
            elif [i, j + 1] == banana:
                print(b, end="")
            elif [i, j + 1] == strawberry:
                print(s, end="")
            elif [i, j + 1] in snake:
                print("*", end="")
            else:
                print(" ", end="")
        print("#")

    for i in range(WIDTH):
        print("#", end="")

    print()


def new_fruits(snake):
    global apple, banana, strawberry, a, b, s
    apple = new_apple(snake)
    banana = new_banana(snake, apple)
    strawberry = new_strawberry(snake, apple, banana)

    a = new_letter(SIMBOLS_UNICAL, '')
    b = new_letter(LnotS, '')
    s = new_letter(LnotS, b)


FIELD_START = r'''
___________
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


SECRET = create_secret()
snake = [random_position()]

SIMBOLS_UNICAL = []
SIMBOLS_LUCKY = []
for i in SECRET:
    if i not in SIMBOLS_UNICAL:
        SIMBOLS_UNICAL.append(i)

k = len(SECRET)


Field = [FIELD_START, FIELD_2, FIELD_3, FIELD_4, FIELD_5,
     FIELD_6, FIELD_7, FIELD_8, FIELD_9, FIELD_FINAL]
Letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LnotS = []

for i in Letter:
    if i not in SIMBOLS_UNICAL:
        LnotS.append(i)
    
FIELD = FIELD_START
n = 0
st = string("")

new_fruits(snake)

with keyboard.Listener(on_press=process_press) as listener:
    while f:
        draw_board(score)
        time.sleep(2)

        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        head = [head_x, head_y]

        if head_x <= 0 or head_y < 0:
            f = False
        elif head_x >= HEIGHT - 1 or head_y >= WIDTH - 1:
            f = False
        elif head in snake and direction != [0, 0]:
            f = False

        snake.insert(0, head)

        if head == apple:
            score += 10

            i = SIMBOLS_UNICAL.index(a)
            SIMBOLS_UNICAL.pop(i)
            
            st = string(a)
#            print(st)

            if st == SECRET:
                f = False
                win = True
            else:
                new_fruits(snake)

        elif head == banana:
            n = n + 1
            FIELD = Field[n]
            
            if FIELD == FIELD_FINAL:
                f = False
            else:
                new_fruits(snake)
                
            snake.pop(-1)

        elif head == strawberry:
            score -= 10
            n = n + 1
            FIELD = Field[n]
            
            if FIELD == FIELD_FINAL:
                f = False
            else:
                new_fruits(snake)
                
            snake.pop(-1)
        else:
            snake.pop(-1)

        
        time.sleep(1)
        pass

print(FIELD)
print(f"score = {score}")

if win:
    print("YOU WIN!!!")
else:
    print("GAME OVER")
