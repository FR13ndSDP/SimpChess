from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece

WHITE = True
BLACK = False


class King(Piece):

    stringRep = "K"
    value = 100

    def __init__(self, board, side, position, movesMade=0):
        super().__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        currentPos = self.position
        movements = [
            C(0, 1),
            C(0, -1),
            C(1, 0),
            C(-1, 0),
            C(1, 1),
            C(1, -1),
            C(-1, -1),
            C(-1, 1),
        ]
        for movement in movements:
            newPos = currentPos + movement
            if self.board.isValidPos(newPos):
                pieceAtNewPos = self.board.pieceAtPosition(newPos)
                if pieceAtNewPos is None:
                    yield Move(self, newPos)
                elif pieceAtNewPos.side != self.side:
                    yield Move(self, newPos, pieceToCapture=pieceAtNewPos)

        # TODO: Castling
