# Developed by Yasir Celtik

import msvcrt
import os
import string
import math


class Board(object):
    def __init__(self, boardX, boardY, fill=' ', border_fill='#'):
        self.boardX = boardX
        self.boardY = boardY
        self.fill = fill
        self.border_fill = border_fill
        # instead of generating a clean board each time i will keep this clean
        # copy and overwrite teh previous board with this clean version
        self.clean_board = self.__clean_and_make_border()
        self.board_print = self.clean_board

    def __clean_and_make_border(self):
        # clear the baord with ' '
        board_print = [[self.fill] * self.boardX] * self.boardY
        # this border function scales to any size of play area
        # and is much much less of a headache than what i had before
        # make the top border
        board_print[0] = self.border_fill * self.boardX
        # make the bottom border
        board_print[self.boardY - 1] = self.border_fill * self.boardX

        # make the side borders which is just the first index and the last index
        # of each row from the Y index of 1 to Y - 2 since we already have the
        # first and last row covered
        for i in range(1, self.boardY - 2):
            board_print[i][0] = self.border_fill
            board_print[i][-1] = self.border_fill

        return board_print

    # problem possibly here
    def draw_board(self):
        for i in self.board_print:
            print(*i, sep='')
            # print(i)

    def clear_board(self):
        self.board_print = self.clean_board

    # problem possibly here
    def draw_snake(self, snake_pos, body_fill):
        for pos in snake_pos:
            self.board_print[pos[1]][pos[0]] = body_fill
            print(pos, self.board_print[pos[1]][pos[0]])


class Snake(object):
    def __init__(self, boardX, boardY, body_fill='@', init_length=4):
        self.body_fill = body_fill
        # initial length of the snake
        # index 0 will be the head
        self.init_length = init_length
        self.boardX = boardX
        self.boardY = boardY
        # the head will start at the center of the baord
        self.startX = math.floor(boardX / 2)
        self.startY = math.floor(boardY / 2)
        # this 2d array will store the positions of the body pieces in [[X,Y]]
        self.body_pos = [[i, self.startY] for i in range(self.startX, self.startX + self.init_length)]
        self.direction = Snake.a

    # movement and quit ascii numbers
    w = 119
    a = 97
    s = 115
    d = 100
    q = 113

    # incomplete
    def move_snake(self, other):
        # check for keybaord hit, will move in previous direction if not hit
        if msvcrt.kbhit():
            # get ascii value of input
            self.direction = ord(msvcrt.getch())
            if self.direction == Snake.w:
                self.body_pos = self.shift_body('Y', -1)
            elif self.direction == Snake.a:
                self.body_pos = self.shift_body('X', -1)
            elif self.direction == Snake.s:
                self.body_pos = self.shift_body('Y', 1)
            elif self.direction == Snake.d:
                self.body_pos = self.shift_body('X', 1)
            elif self.direction == Snake.q:
                exit()
            print(Snake.a)
        # else:

    # incomplete? maybe seems to work
    def shift_body(self, direction, move):
        # new list of pody pos which will have every element shifted by 1 to
        # make space for the new head, old tail gets auto overwritten
        new_body = [[]]
        for i in range(len(self.body_pos - 1)):
            new_body.append(self.body_pos[i + 1])
        if direction == 'X':
            # get teh old head pos and put it into the new head pos
            new_body[0] = [new_body[1][0] + move, new_body[1][1]]
            return new_body
        elif direction == 'Y':
            # get teh old head pos and put it into the new head pos
            new_body[0] = [new_body[1][0], new_body[1][1] + move]
            return new_body


def draw(main_board, main_snake):
    # os.system('cls')
    main_board.clear_board()  # get empty board with borders
    main_board.draw_snake(main_snake.body_pos, main_snake.body_fill)
    main_board.draw_board()  # draw board with snake
    print(main_snake.body_pos)  # for debug, print positions for snake body


main_board = Board(20, 10)
main_snake = Snake(main_board.boardX, main_board.boardY)
# while True:
draw(main_board, main_snake)
# main_snake.move_snake(main_board)
