# coding:utf-8

from Bishop import Bishop
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
from Rook import Rook
# from King import King
from Coordinate import Coordinate as C
from Move import Move
from termcolor import colored

WHITE = True
BLACK = False

class Board:
    def __init__(self, castleBoard=False, passant=False, promotion=False):
        self.pieces = []
        self.history = []
        self.points = 0
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False

        self.pieces.extend(
            [
                Rook(self, BLACK, C(0, 7)),
                Knight(self, BLACK, C(1, 7)),
                Bishop(self, BLACK, C(2, 7)),
                Queen(self, BLACK, C(3, 7)),
                #King(self, BLACK, C(4, 7)),
                Bishop(self, BLACK, C(5, 7)),
                Knight(self, BLACK, C(6, 7)),
                Rook(self, BLACK, C(7, 7))
            ]
        )
        for x in range(8):
            self.pieces.append(Pawn(self, BLACK, C(x, 6)))
            self.pieces.append(Pawn(self, WHITE, C(x, 1)))
        
        self.pieces.extend(
            [
                Rook(self, WHITE, C(0, 0)),
                Knight(self, WHITE, C(1, 0)),
                Bishop(self, WHITE, C(2, 0)),
                Queen(self, WHITE, C(3, 0)),
                #King(self, WHITE, C(4, 0)),
                Bishop(self, WHITE, C(5, 0)),
                Knight(self, WHITE, C(6, 0)),
                Rook(self, WHITE, C(7, 0))
            ]
        )

    def __str__(self):
        return self.makeStringRep(self.pieces)

    def makeStringRep(self, pieces):
        stringRep = ""
        for y in range(7, -1, -1):
            for x in range(8):
                piece = None
                for p in pieces:
                    if p.position == C(x, y):
                        piece = p
                        break
                pieceRep = ""
                if piece:
                    side = piece.side
                    color = "blue" if side == WHITE else "red"
                    pieceRep = colored(piece.stringRep, color)
                else:
                    pieceRep = "•"
                stringRep += pieceRep + " "
            stringRep += "\n"
        return stringRep.rstrip()

if __name__ == "__main__":
    board = Board()
    print(board)
