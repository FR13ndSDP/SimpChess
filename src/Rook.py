from Coordinate import Coordinate as C
from Piece import Piece

WHITE = True
BLACK = False

class Rook(Piece):

    stringRep = "R"
    value = 5

    def __init__(self, side, position, movesMade=0):
        super().__init__(side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        currentPosition = self.position

        directions = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0)]
        for direction in directions:
            for move in self.movesInDirectionFromPos(
                currentPosition, direction, self.side
            ):
                yield move

if __name__ == "__main__":
    r = Rook(WHITE, C(1, 1), 0)
    for i in r.getPossibleMoves():
        print(i)
