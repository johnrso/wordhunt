from board import Board
import time

class GraphSolver:

    def __init__(self, board):
        self.board = board

    def traverse(self, sq, seen = set(), word = ""):
        if (sq.coord not in seen):
            seen.add(sq.coord)
            word += sq.letter
            if len(word) < 8:
                for neighbor in sq.neighbors:
                    self.traverse(self.board.getSquare(neighbor[0], neighbor[1]), seen, word)
            if self.board.check_word(word) and len(word) >= 3:
                self.board.add_word(word)
            seen.remove(sq.coord)

    def solve(self):
        for row in range(self.board.width):
            for column in range(self.board.height):
                self.traverse(self.board.getSquare(row, column))

    def endGame(self, full = False, outputFile = ""):
        self.board.endGame(full, outputFile);

    def getScore(self):
        return self.board.score

    def measurePerformance(dict, trials = 100):
        total = 0
        words = 0

        for i in range(trials):
            t0 = time.perf_counter()
            b = Board(dict)

            print(b)
            s = GraphSolver(b)
            s.solve()
            t1 = time.perf_counter()

            elapsed = t1 - t0
            total += elapsed
            words += b.numWords()

            print("TIME FOR TRIAL " + str(i) + ": " + f"{elapsed:.2f}" + ' sec')
            print("SCORE: " + str(s.getScore()))
            print("WORDS FOUND: " + str(s.board.numWords()))

        total /= trials
        words /= trials

        print()
        print("AVERAGE TIME: " + f"{total:.2f}")
        print("AVERAGE WORDS FOUND: " + str(words))
        print()

class GeneticSolver:

    def __init__(self, board, weights):
        pass
