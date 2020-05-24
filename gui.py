import pyglet
from widgets import BoardWidget, SquareWidget
from board import Board

width, height = 800, 600
window = pyglet.window.Window(width, height)

board = Board(dict = './dictionaries/webster_dictionary.json', dimensions = (width, height))

b = BoardWidget(board)

score_label = pyglet.text.Label(text="Score: 10", font_name = 'Helvetica', x=10, y=460)
level_label = pyglet.text.Label(text="My Amazing Game",
                            x = window.width//2, y=window.height//2, anchor_x='center')

@window.event
def on_draw():
    window.clear()

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
        [0, 1, 2, 3],
        ('v2i', (0, 0,
                 0, height,
                 width, height,
                 width, 0))
    )

    batch = pyglet.graphics.Batch()
    b.draw_board(batch)
    batch.draw()

def update(dt):
    b.update(dt)
    
pyglet.clock.schedule_interval(update,1/60.0)

if __name__ == '__main__':
    pyglet.app.run()
