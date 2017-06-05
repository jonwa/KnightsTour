#!/usr/bin/python

import sys
import numpy

class KnightsTour:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = numpy.zeros([w, h])

    def print_board(self):
        for y in range(self.h):
            for x in range(self.w):
                print(int(self.board[x][y]), end="\t")
            print()
            print()

    def is_valid(self, pos):
        return (pos[0] >= 0 and pos[0] < self.w and 
                pos[1] >= 0 and pos[1] < self.h and 
                self.board[pos[0]][pos[1]] == 0)

    def get_neighbours(self, pos):
        result = []
        moves = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        for move in moves:
            new_pos = [pos[0] + move[0], pos[1] + move[1]]
            if self.is_valid(new_pos):
                result.append(new_pos)
        return result

    def move(self, pos):
        result = None
        min_weight = sys.maxsize
        neighbours = self.get_neighbours(pos)
        for neighbour in neighbours:
            curr_weight = len(self.get_neighbours(neighbour))
            if curr_weight < min_weight:
                result = neighbour
                min_weight = curr_weight
        return result

    def solve(self, pos, n):
        self.board[pos[0]][pos[1]] = n
        if n == self.w * self.h:
            self.print_board()
            sys.exit(1)
        else:
            self.solve(self.move(pos), n + 1)
            self.board[pos[0]][pos[1]] = 0

if __name__ == '__main__':
    kt = KnightsTour(8, 8)
    kt.solve([0, 0], 1)

