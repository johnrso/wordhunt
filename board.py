import numpy as np
import random
from weights import Alphabet

class Board:

    points = (0, 0, 0, 300, 400, 800, 1400, 1800, 2000, 0, 0)

    def __init__(self, dict = 'words_dictionary.json', alpha = None):
        self.words = []
        self.letters_used = {}
        self.board = []
        self.points = 0

        a = Alphabet(dict)

        if alpha is None:
            alpha = a.letters

        weights = a.generate_weights(alpha)

        for i in range(4):
            row = []
            for j in range(4):
                 row += [Square(i,
                 j,
                 np.random.choice([*weights], 1, p = list(weights.values())).item())]
            self.board += [row]

    def __str__(self):
        string = '\nSCORE: ' + str(self.points)
        string += '\n\n'
        for i in self.board:
            row = '   '
            for j in i:
                row += str(j) + ' '
            string += row + '\n'

        return string

    def __repr__(self):
        return str(self.board)

    def score(self, word):
        self.words += word
        for letter in word:
            self.add_letters(letter)

    def add_letters(self, letter):
        if letter not in letters_used:
            letters_used[letter] = 1
        else:
            letters_used[letter] += 1

    def getSquare(self, row, column):
        try:
            return self.board[row][column]
        except IndexError as e:
            print("IndexError")
            return null

class Square:

    inst = {}

    def __init__(self, row, column, letter):
        self.coord = (row, column)
        self.neighbors = []
        Square.inst[self.coord] = self
        self.generateNeighbors(row, column)
        self.letter = letter

        print(len(self.neighbors), self.letter, self.coord)

    def __str__(self):
        return self.letter

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (isinstance(other, Square) and self.coord == other.coord
        and self.letter == other.letter)

    def generateNeighbors(self, row, column):
        for i in range(max(0, row - 1), min(4, row + 2)):
            for j in range(max(0, column - 1), min(4, column + 2)):
                if (i,j) != self.coord:
                    self.neighbors += [(i,j)]

b = Board()