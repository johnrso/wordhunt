import numpy as np
import random
from weights import Alphabet

class Board:

    points = (0, 0, 0, 300, 400, 800, 1400, 1800, 2000, 0, 0)
    width = height = 4

    def __init__(self, dict = 'words_dictionary.json', alpha = None, letters = []):
        self.words = set()
        self.letters_used = {}
        self.board = []
        self.score = 0
        self.dict = Alphabet(dict)

        if alpha is None:
            alpha = self.dict.letters

        weights = self.dict.generate_weights(alpha)
        if (letters == []):
            for i in range(Board.width):
                row = []
                for j in range(Board.height):
                     row += [Square(i, j, np.random.choice([*weights],
                     1, p = list(weights.values())).item())]
                self.board += [row]
        else:
            index = 0
            for i in range(Board.width):
                row = []
                for j in range(Board.height):
                     row += [Square(i,j, letters[index])]
                     index += 1
                self.board += [row]


    def __str__(self):
        string = '\nSCORE: ' + str(self.score)
        string += '\n\n'
        for i in self.board:
            row = '   '
            for j in i:
                row += str(j) + ' '
            string += row + '\n'

        return string

    def __repr__(self):
        return str(self.board)

    def check_word(self, word):
        return self.dict.check_word(word);

    def add_word(self, word):
        self.words.add(word)
        self.score += Board.points[len(word)]
        for letter in word:
            self.add_letters(letter)

    def add_letters(self, letter):
        if letter in self.letters_used:
            self.letters_used[letter] += 1
        else:
            self.letters_used[letter] = 1

    def getSquare(self, row, column):
        try:
            return self.board[row][column]
        except IndexError as e:
            print("IndexError")
            return null

    def endGame(self):
        print("SCORE: " + str(self.score))
        print("TOTAL WORDS FOUND: "  + str(len(self.words)))
        print()
        listWords = list(self.words)
        listWords.sort(reverse = True, key = lambda word: len(word))
        for i in range(1, min(21, len(listWords) + 1)):
            print(str(i) + ": " + listWords[i - 1])

        print()

class Square:

    inst = {}

    def __init__(self, row, column, letter):
        self.coord = (row, column)
        self.neighbors = []
        Square.inst[self.coord] = self
        self.generateNeighbors(row, column)
        self.letter = letter

    def __str__(self):
        return self.letter

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (isinstance(other, Square) and self.coord == other.coord
        and self.letter == other.letter)

    def generateNeighbors(self, row, column):
        for i in range(max(0, row - 1), min(Board.width, row + 2)):
            for j in range(max(0, column - 1), min(Board.height, column + 2)):
                if (i,j) != self.coord:
                    self.neighbors += [(i,j)]
