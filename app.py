from flask import Flask, render_template, request

app = Flask(__name__)

tiles = ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️']
turn = 'X'
gameover = False

def check_winner(board):
    board = list(board)
    
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    # Check each winning combination
    for combo in win_combinations:
        # Get values at current combination positions
        a, b, c = board[combo[0]], board[combo[1]], board[combo[2]]
        
        # Check if all three positions match and are either X or O
        if a == b == c and a in ['X', 'O']:
            return a
    
    # No winner found
    return None

@app.route('/x')
def x():
    global turn
    global gameover
    tile = request.args.get('tile')
    reset = request.args.get('reset')
    if tile != None and gameover == False:
        if tiles[int(tile) - 1] == '⬜️':  
            if turn == 'X':
                tiles[int(tile) - 1] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
    elif reset != None:
        for i in range(9):
            tiles[i] = '⬜️'
        turn = 'X'
        gameover = False
    winner = check_winner(tiles)
    if winner != None:
        gameover = True
        winner += ' wins!'
    else:
        winner = ''
    return render_template('ttt.html', tile1=tiles[0], tile2=tiles[1], tile3=tiles[2], tile4=tiles[3], tile5=tiles[4], tile6=tiles[5], tile7=tiles[6], tile8=tiles[7], tile9=tiles[8], player='X', turn=turn, winner=winner)

@app.route('/o')
def o():
    global turn
    global gameover
    tile = request.args.get('tile')
    reset = request.args.get('reset')
    if tile != None and gameover == False:
        if tiles[int(tile) - 1] == '⬜️': 
            if turn == 'O': 
                tiles[int(tile) - 1] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
    elif reset != None:
        for i in range(9):
            tiles[i] = '⬜️'
        turn = 'X'
        gameover = False
    winner = check_winner(tiles)
    if winner != None:
        gameover = True
        winner += ' wins!'
    else:
        winner = ''
    return render_template('ttt.html', tile1=tiles[0], tile2=tiles[1], tile3=tiles[2], tile4=tiles[3], tile5=tiles[4], tile6=tiles[5], tile7=tiles[6], tile8=tiles[7], tile9=tiles[8], player='O', turn=turn, winner=winner)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spectator')
def spectator():
    global turn
    global gameover
    winner = check_winner(tiles)
    if winner != None:
        gameover = True
        winner += ' wins!'
    else:
        winner = ''
    return render_template('spectator.html', tile1=tiles[0], tile2=tiles[1], tile3=tiles[2], tile4=tiles[3], tile5=tiles[4], tile6=tiles[5], tile7=tiles[6], tile8=tiles[7], tile9=tiles[8], player='X', turn=turn, winner=winner)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1145, debug=False)