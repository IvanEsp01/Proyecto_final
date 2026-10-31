"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# MODIFICACIÓN 3: Reducido a 8 números duplicados (16 fichas en total para un 4x4)
tiles = list(range(8)) * 2
state = {'mark': None}
# MODIFICACIÓN 3: El tablero de 4x4 tiene 16 casillas
hide = [True] * 16

# MODIFICACIÓN 1: Variables para el contador y el sistema de escritura
pairs_found = 0
writer = Turtle(visible=False)


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # MODIFICACIÓN 3: Ajustado a 4 columnas y rango de -100 a 100
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # MODIFICACIÓN 3: Coordenadas centradas para la cuadrícula 4x4
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global pairs_found
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
        # MODIFICACIÓN 1: Incrementamos el contador de pares encontrados
        pairs_found += 1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # MODIFICACIÓN 3: Dibujar las 16 casillas de la cuadrícula 4x4
    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    
    # Limpiamos el texto anterior para actualizar la interfaz
    writer.clear()
    
    # MODIFICACIÓN 1: Mostrar el contador de pares en la esquina superior
    writer.up()
    writer.goto(-180, 185)
    writer.color('blue')
    writer.write(f'Pares encontrados: {pairs_found}', font=('Arial', 14, 'normal'))

    # MODIFICACIÓN 2: Mensaje de Victoria (8 pares en total para el tablero 4x4)
    if pairs_found == 8:
        writer.goto(-80, 0)
        writer.color('green')
        writer.write('¡Victoria!', font=('Arial', 30, 'bold'))
        return  # Detiene el bucle al ganar

    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()