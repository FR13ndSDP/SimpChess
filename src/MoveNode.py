class MoveNode:
    def __init__(self, move, children, parent) -> None:
        self.move = move
        self.children = children
        self.parent = parent
        self.point = None
        self.depth = 1

    def __str__(self) -> str:
        stringRep = (
            "Move : "
            + str(self.move)
            + " Point : "
            + str(self.point)
            + " Checkmate : "
            + str(self.move.checkmate)
            + "\n"
        )

        for child in self.children:
            stringRep += str(child)
            stringRep += "\n"
        return stringRep

    def __gt__(self, other):
        if self.move.checkmate and not other.move.checkmate:
            return True
        if not self.move.checkmate and other.move.checkmate:
            return False
        if self.move.checkmate and other.move.checkmate:
            return False
        return self.point > other.point

    def __lt__(self, other):
        if self.move.checkmate and not other.move.checkmate:
            return False
        if not self.move.checkmate and other.move.checkmate:
            return True
        if self.move.checkmate and other.move.checkmate:
            return False
        return self.point < other.point

    def __eq__(self, other):
        if self.move.checkmate and other.move.checkmate:
            return True
        return self.point == other.point

    
    def getDepth(self):
        depthCnt = 1
        highestNode = self
        while True:
            if highestNode.parent is not None:
                highestNode = highestNode.parent
                depthCnt += 1
            else:
                return depthCnt

