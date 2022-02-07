from Coordinate import Coordinate as C
from Piece import Piece
from Move import Move
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from Rook import Rook

WHITE = True
BLACK = False


class Pawn(Piece):

    stringRep = "P"
    value = 1

    def __init__(self, board, side, position, movesMade=0):
        super().__init__(board, side, position)
        self.movesMade = movesMade

    # yield moves without evaluate if it's valid
    def getPossibleMoves(self):
        currentPosition = self.position

        # Pawn moves one up
        movement = C(0, 1) if self.side == WHITE else C(0, -1)
        advanceOnePosition = currentPosition + movement
        if self.board.isValidPos(advanceOnePosition):
            # Promotion moves
            if self.board.pieceAtPosition(advanceOnePosition) is None:
                col = advanceOnePosition[1]
                if col == 7 or col == 0:
                    piecesForPromotion = [
                        Rook(self.board, self.side, advanceOnePosition),
                        Knight(self.board, self.side, advanceOnePosition),
                        Bishop(self.board, self.side, advanceOnePosition),
                        Queen(self.board, self.side, advanceOnePosition),
                    ]
                    for piece in piecesForPromotion:
                        move = Move(self, advanceOnePosition)
                        move.promotion = True
                        move.specialMovePiece = piece
                        yield move
                else:
                    yield Move(self, advanceOnePosition)

        # Pawn moves two up
        if self.movesMade == 0:
            movement = C(0, 2) if self.side == WHITE else C(0, -2)
            advanceTwoPosition = currentPosition + movement
            if self.board.isValidPos(advanceTwoPosition):
                if (
                    self.board.pieceAtPosition(advanceTwoPosition) is None
                    and self.board.pieceAtPosition(advanceOnePosition) is None
                ):
                    yield Move(self, advanceTwoPosition)

        # TODO: Pawn takes

        # TODO: En passant
