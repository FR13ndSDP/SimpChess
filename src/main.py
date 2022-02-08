import random
import sys
import re
from Board import Board

WHITE = True
BLACK = False


def makeRandomMove(board):
    moves = board.getAllMovesLegal()
    move = random.choice(moves)
    board.makeMove(move)
    print("All moves: %d" % len(moves))


def parseInput(board, notation):
    regexNotation = re.compile("[a-h][1-8][a-h][1-8]")
    if regexNotation.match(notation):
        return moveForCoordinateNotation(board, notation)
    raise ValueError("Invalid move : %s" % notation)


def moveForCoordinateNotation(board, notation):
    for move in board.getAllMovesLegal():
        if (
            board.positionToHumanCoord(move.oldPos) == notation[0:2]
            and board.positionToHumanCoord(move.newPos) == notation[2:4]
        ):
            return move
    raise ValueError("Illegal move : %s" % notation)


if __name__ == "__main__":
    playSide = WHITE
    board = Board()
    print(board)
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
                makeRandomMove(board)
                print(board)
    except KeyboardInterrupt:
        sys.exit()