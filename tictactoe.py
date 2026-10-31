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



state = {
    'player': 0,
    'board': {},
    'game_over': False
}

players = [drawx, drawo]


def check_winner(player):
    """Check if a player has three symbols in a row."""
    board = state['board']

    winning_combinations = [
        [(-200, -200), (-67, -200), (66, -200)],
        [(-200, -67), (-67, -67), (66, -67)],
        [(-200, 66), (-67, 66), (66, 66)],
        [(-200, -200), (-200, -67), (-200, 66)],
        [(-67, -200), (-67, -67), (-67, 66)],
        [(66, -200), (66, -67), (66, 66)],
        [(-200, -200), (-67, -67), (66, 66)],
        [(66, -200), (-67, -67), (-200, 66)]
    ]

    for combination in winning_combinations:
        if all(board.get(square) == player for square in combination):
            return True

    return False


def tap(x, y):
    """Draw X or O in tapped square."""
    if state['game_over']:
        return

    # Check if the click is inside the board
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    x = floor(x)
    y = floor(y)

    # Check if the selected square is already occupied
    if (x, y) in state['board']:
        return

    player = state['player']
    draw = players[player]

    draw(x, y)

    # Register the occupied square
    state['board'][(x, y)] = player

    update()

    # Check if the current player has won
    if check_winner(player):
        message = 'Player X wins!' if player == 0 else 'Player O wins!'
        state['game_over'] = True

    # Check if all squares are occupied
    elif len(state['board']) == 9:
        message = "It's a tie!"
        state['game_over'] = True

    else:
        state['player'] = 1 - player
        return

    # Display the final result
    color('black')
    up()
    goto(0, -235)
    write(message, align='center', font=('Arial', 16, 'bold'))
    update()

    print(message)


setup(500, 500, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
