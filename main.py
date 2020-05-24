#!/usr/bin/env python
from board import Board
from solver import GraphSolver
from player import Player
import string
import sys
import getopt

def main(argv):
    inputFile = ''
    outputFile = ''
    dictionary = './dictionaries/webster_dictionary.json'
    test = False
    random = False
    full = False

    try:
        opts, args = getopt.getopt(argv,"d:i:o:trf",)
    except getopt.GetoptError:
        print('Invalid command.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-i":
            inputFile = arg
        elif opt == "-o":
            outputFile = arg
        elif opt == "-d":
            dictionary = arg
        elif opt == "-t":
            test = True
        elif opt == '-r':
            random = True
        elif opt == '-f':
            full = True

    if test:
        GraphSolver.measurePerformance(dict = dictionary)
        sys.exit(1)

    if inputFile == "" and not random:
        inputs = []
        print("Please enter the letters of the board by row, one at a time.")

        for i in range(16):
            letter = input(str(i + 1) + " >>> ").lower()
            while (len(letter) != 1 or letter not in string.ascii_lowercase):
                print("Invalid input.")
                letter = input(str(i + 1) + " >>> ").lower()
            inputs.append(letter)

        b = Board(dictionary, letters = inputs)

    elif inputFile == "" and random:
        b = Board(dictionary)

    else:
        pass #handle scanning in here

    print(b)
    print("Solving board.")
    print()

    s = GraphSolver(b)
    s.solve()

    p = Player(b, s.getSolutions())
    p.play()
    b.endGame(full, outputFile)
    sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])
