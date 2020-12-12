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
        # clear the board with ' '
        board_print = [[self.fill for y in range(self.boardY)] for x in range(self.boardX)]

        for x in range(self.boardX):
            for y in range(self.boardY):
                # border coordinates
                if x == 0 or y == 0 or y == self.boardY - 1 or x == self.boardX - 1:
                    board_print[x][y] = self.border_fill
                # non-border coordinates
                else:
                    board_print[x][y] = self.fill

        return board_print

    # problem possibly here
    def draw_board(self):
        board_result = ""
        for y in range(self.boardY):
            for x in range(self.boardX):
                board_result += self.board_print[x][y]
            board_result += "\n"
        print(board_result)

    def clear_board(self):
        self.board_print = self.clean_board

    # problem possibly here
    def draw_snake(self, snake):
        for pos in snake.body_pos:
            self.board_print[pos[0]][pos[1]] = snake.body_fill
            # print(pos, self.board_print[pos[0]][pos[1]])


class Snake(object):
    # movement and quit ascii numbers
    w = 119
    a = 97
    s = 115
    d = 100
    q = 113

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
        # this list will store the positions of the body pieces as tuples (x, y)
        self.body_pos = [(i, self.startY) for i in range(self.startX, self.startX + self.init_length)]
        self.direction = Snake.a

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
    os.system('cls')
    main_board.clear_board()  # get empty board with borders
    main_board.draw_snake(main_snake)
    main_board.draw_board()  # draw board with snake
    # print(main_snake.body_pos)  # for debug, print positions for snake body


main_board = Board(20, 10)
main_snake = Snake(main_board.boardX, main_board.boardY)
while True:
    draw(main_board, main_snake)
    #main_snake.move_snake(main_board)
