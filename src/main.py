import random
import sys
import re
from Board import Board
from MoveNode import MoveNode
from AI import AI
WHITE = True
BLACK = False


'''
def humanCoordToPosition(coord):
    transTable = str.maketrans("abcdefgh", "12345678")
    coord = coord.translate(transTable)
    coord = [int(c) - 1 for c in coord]
    pos = C(coord[0], coord[1])
    return pos
'''

def positionToHumanCoord(pos):
    transTable = str.maketrans("01234567", "abcdefgh")
    notation = str(pos[0]).translate(transTable) + str(pos[1] + 1)
    return notation

def parseInput(board, notation):
    regexNotation = re.compile("[a-h][1-8][a-h][1-8]")
    if regexNotation.match(notation):
        return moveForCoordinateNotation(board, notation)
    raise ValueError("Invalid move : %s" % notation)


def moveForCoordinateNotation(board, notation):
    for move in board.getAllMovesLegal():
        if (
            positionToHumanCoord(move.oldPos) == notation[0:2]
            and positionToHumanCoord(move.newPos) == notation[2:4]
        ):
            return move
    raise ValueError("Illegal move : %s" % notation)


if __name__ == "__main__":
    playSide = WHITE
    board = Board()
    print(board)
    ai = AI(board, not playSide, 2)
    try:
        while True:
            if board.isCheckmate():
                print("CHECKMATE!")
                sys.exit()
            if playSide == board.currentSide:
                command = input("your move : ")
                move = parseInput(board, command)
                board.makeMove(move)
            else:
                ai.makeBestMove()
                print(board)
    except KeyboardInterrupt:
        sys.exit()
    '''
    moves = board.getAllMovesLegal()
    move_first = random.choice(moves)
    board.makeMove(move_first)
    print(board)
    moves = board.getAllMovesLegal()
    move_second = random.choice(moves)
    board.makeMove(move_second)
    print(board)
    moves = board.getAllMovesLegal()
    node = MoveNode(move_second, children=moves, parent=move_first)
    print(node)
    '''
