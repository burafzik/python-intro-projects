from pynput import keyboard
from random import randint
from common.util import clear_terminal
import time

TERM_FLAG = "IDLE"

WIDTH, HEIGHT = 20, 20
direction = [0, 0]


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


def draw_board(score):
    cls()

    print(apple)
    print(snake)
    print(direction)
    print(f"score = {score}")

    for i in range(WIDTH):
        print("#", end="")

    print()

    for j in range(HEIGHT - 2):
        print("#", end="")
        for i in range(1, WIDTH - 1):
            if [i, j + 1] == apple:
                print("@", end="")
            elif [i, j + 1] == banana:
                print(")", end="")
            elif [i, j + 1] == strawberry:
                print("&", end="")
            elif [i, j + 1] in snake:
                print("*", end="")
            else:
                print(" ", end="")
        print("#")

    for i in range(WIDTH):
        print("#", end="")

    print()


f = True
snake = [random_position()]
apple = new_apple(snake)
banana = new_banana(snake, apple)
strawberry = new_strawberry(snake, apple, banana)
score = 0

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
        elif head in snake:
            f = False

        print(snake)
        print(head)

        snake.insert(0, head)
        print(snake)

        if head == apple:
            score += 10
            apple = new_apple(snake)
            banana = new_banana(snake, apple)
            strawberry = new_strawberry(snake, apple, banana)
        elif head == banana:
            apple = new_apple(snake)
            banana = new_banana(snake, apple)
            strawberry = new_strawberry(snake, apple, banana)
            snake.pop(-1)
        elif head == strawberry:
            score -= 10
            apple = new_apple(snake)
            banana = new_banana(snake, apple)
            strawberry = new_strawberry(snake, apple, banana)
            snake.pop(-1)
        else:
            snake.pop(-1)
        time.sleep(2)
        pass

print("GAME OVER")
print(score)
