from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece

WHITE = True
BLACK = False


class Knight(Piece):

    stringRep = "N"
    value = 3

    def __init__(self, board, side, position, movesMade=0):
        super().__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        board = self.board
        currentPos = self.position
        movements = [
            C(2, 1),
            C(2, -1),
            C(-2, 1),
            C(-2, -1),
            C(1, 2),
            C(1, -2),
            C(-1, -2),
            C(-1, 2),
        ]
        for movement in movements:
            newPos = currentPos + movement
            if board.isValidPos(newPos):
                pieceAtNewPos = board.pieceAtPosition(newPos)
                if pieceAtNewPos is None:
                    yield Move(self, newPos)
                elif pieceAtNewPos != self.side:
                    yield Move(self, newPos, pieceToCapture=pieceAtNewPos)


if __name__ == "__main__":
    n = Knight(WHITE, C(1, 1), 1)
    for i in n.getPossibleMoves():
        print(i)
