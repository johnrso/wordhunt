from board import Board
import pyglet

class SquareWidget:

    widthpx = heightpx = 100
    offsetpx = 40

    def __init__(self, sq):
        self.square = sq
        self.column = 3 - sq.coord[0]
        self.row = sq.coord[1]
        self.letter = sq.letter

    def draw_square(self, batch):
        x = SquareWidget.offsetpx + (self.row + .5) * SquareWidget.widthpx
        y = SquareWidget.offsetpx + (self.column + .5) * SquareWidget.heightpx
        dx = SquareWidget.widthpx / 2 - 2
        dy = SquareWidget.heightpx / 2 - 2
        coords = (x - dx, y - dy,
                  x - dx, y + dy,
                  x + dx, y + dy,
                  x + dx, y - dy)

        colors = (176, 157, 33) * 4
        vertex_list = pyglet.graphics.vertex_list_indexed(4, [0, 1, 2, 3],
        ('v2f', coords), ('c3B', colors))

        vertex_list.draw(pyglet.gl.GL_QUADS)
        pyglet.text.Label(text = self.letter,font_name = 'Helvetica',
        x = x, y = y, font_size=36, bold = True, anchor_x = 'center',
        anchor_y = 'center', color = (0,0,0,255)).draw()

    def update(self, dt):
        pass

class BoardWidget:

    width = height = 4
    widthpx = heightpx = 408
    offsetpx = 36

    def __init__(self, game):
        self.game = game
        self.board = []

        print(self.game)
        for i in range(self.game.width):
            row = []
            for j in range(self.game.height):
                row += [SquareWidget(self.game.getSquare(i,j))]
            self.board += [row]

    def draw_board(self, batch):
        coords = (BoardWidget.offsetpx, BoardWidget.offsetpx,
                  BoardWidget.offsetpx + BoardWidget.widthpx, BoardWidget.offsetpx,
                  BoardWidget.offsetpx + BoardWidget.widthpx, BoardWidget.offsetpx + BoardWidget.heightpx,
                  BoardWidget.offsetpx, BoardWidget.offsetpx + BoardWidget.heightpx)

        colors = (39, 156, 58) * 4
        vertex_list = pyglet.graphics.vertex_list_indexed(4, [0, 1, 2, 3],
        ('v2f', coords), ('c3B', colors))
        vertex_list.draw(pyglet.gl.GL_QUADS)


        for i in range(BoardWidget.width):
            for j in range(BoardWidget.height):
                self.getSquare(i, j).draw_square(batch)

    def getSquare(self, row, column):
        try:
            return self.board[row][column]
        except IndexError as e:
            print("IndexError")
            return null


    def update(self, dt):
        pass
