from Coordinate import Coordinate as C
from Piece import Piece

WHITE = True
BLACK = False

class Knight(Piece):

    stringRep = "N"
    value = 3

    def __init__(self, side, position, movesMade=0):
        super().__init__(side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        currentPos = self.position

        movements = [
            C(2, 1),
            C(2, -1),
            C(-2, 1),
            C(-2,-1),
            C(1, 2),
            C(1, -2),
            C(-1, -2),
            C(-1, 2)
        ]
        for movement in movements:
            newPos = currentPos + movement
            yield newPos

if __name__ == "__main__":
    n = Knight(WHITE, C(1,1), 1)
    for i in n.getPossibleMoves():
        print(i)   
        