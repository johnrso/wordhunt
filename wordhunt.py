#!/usr/bin/env python

import numpy as np
import weights
import words
import string

words = words.gen_words()
alphabet = list(string.ascii_lowercase)
weights = weights.gen_weights(alphabet)

class Board:

    points = [0, 0, 0, 300, 400, 800, 1400, 1800, 2000, 0, 0]
    width = 4
    height = 4

    def __init__(self, pool = alphabet, dictionary = words):
        self.words = []
        self.letters_used = {}
        self.board = [] # should be np array
        self.points = 0

        for _ in range(self.height):
            self.board += [[np.random.choice(pool, p = weights) for _ in range(self.width)]] # set using choice to make 2d arrays

    def __str__(self):
        str = '\n'
        for i in self.board:
            row = ''
            for j in i:
                row += j + ' '
            str += row + '\n'
        return str

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

    def form_word(self, word, letters_used):
