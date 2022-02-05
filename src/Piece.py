from Coordinate import Coordinate as C

WHITE = True
BLACK = False
X = 0
Y = 1

class Piece:
    def __init__(self, side, position, movesMade=0):
        self.side = side
        self.position = position
        self.movesMade = 0

    # 打印Piece的魔法方法
    def __str__(self):
        sideString = "White" if self.side == WHITE else "Black"
        return (
            "Type : "
            + type(self).__name__
            + " - String : "
            + str(self.stringRep)
            + " - Position : "
            + str(self.position)
            + " - Side : "
            + sideString
            + " -- Value : "
            + str(self.value)
            + " -- Moves made : "
            + str(self.movesMade)
        )

    def __eq__(self, other):
        if (
            self.side == other.side
            and self.position == other.position
            and self.__class__ == other.__class__
        ):
            return True
        return False

    def copy(self):
        cpy = self.__class__(
            self.side, self.position, self.movesMade
        )
        return cpy

    # TODO: movesInDirectionFromPos
    # Get all moves in direction
    def movesInDirectionFromPos(self, pos, direction, side):
        for dis in range(1, 8):
            movement = C(dis * direction[X], dis * direction[Y])
            newPos = pos + movement
            yield newPos