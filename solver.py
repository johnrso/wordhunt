from board import Board

class GraphSolver:

    def __init__(self, board):
        self.board = board

    def traverse(self, sq, seen = set(), word = ""):
        if (sq.coord not in seen):
            seen.add(sq.coord)
            word += sq.letter
            for neighbor in sq.neighbors:
                self.traverse(self.board.getSquare(neighbor[0], neighbor[1]), seen, word)
            if self.board.check_word(word) and len(word) >= 3:
                self.board.add_word(word)
            seen.remove(sq.coord)

    def solve(self):
        for row in range(self.board.width):
            for column in range(self.board.height):
                self.traverse(self.board.getSquare(row, column))

        self.board.endGame();

class GeneticSolver:

    def __init__(self, board, weights):
        pass
