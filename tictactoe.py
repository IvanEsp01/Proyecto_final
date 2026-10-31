"""Tic Tac Toe

Descarga el código con el comando indicado previamente, ejecuta el juego, analiza el código y, una vez comprendido, 
realizar las siguientes modificaciones:
1. Modificar el tamaño y el color de los símbolos "X" y "O" y centrarlos.
2. Validar si una casilla ya se encuentra ocupada.
3. Determinar cuando juego haya terminado e indicar quién ganó o si se empató.

"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)



def drawx(x, y):
    """Draw X player."""
    color('blue')
    width(8)
    line(x + 25, y + 25, x + 108, y + 108)
    line(x + 25, y + 108, x + 108, y + 25)


def drawo(x, y):
    """Draw O player."""
    color('red')
    width(8)
    up()
    goto(x + 66.5, y + 24)
    down()
    circle(42)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
