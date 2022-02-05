from Coordinate import Coordinate as C
from Piece import Piece

WHITE = True
BLACK = False

class Pawn(Piece):

    stringRep = "P"
    value = 1

    def __init__(self, side, position, movesMade=0):
        super().__init__(side, position)
        self.movesMade = movesMade

    # yield moves without evaluate if it's valid
    def getPossibleMoves(self):
        currentPosition = self.position

        # Pawn moves one up
        movement = C(0, 1) if self.side == WHITE else C(0, -1)
        advanceOnePosition = currentPosition + movement
        yield advanceOnePosition

        # Pawn moves two up
        if self.movesMade == 0:
            movement = C(0, 2) if self.side == WHITE else C(0, -2)
            advanceTwoPosition = currentPosition + movement
            yield advanceTwoPosition

        # TODO: Pawn takes

        # TODO: En passant


if __name__ == "__main__":
    p = Pawn(WHITE, C(0, 1), 1)
    p_cpy = p.copy()
    print(p)
    print(p_cpy)
    print( p == p_cpy)
    print("possible moves: ")
    moves = p.getPossibleMoves()
    for i in moves:
        print(i)