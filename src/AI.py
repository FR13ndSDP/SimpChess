import random
from Board import Board
from MoveNode import MoveNode

WHITE = True
BLACK = False


class AI:

    depth = 1
    board = None
    side = None
    
    def __init__(self, board, side, depth) -> None:
        self.board = board
        self.side = side
        self.depth = depth

    def getFirstMove(self):
        move = list(self.board.getAllMovesLegal())[0]
        return move

    def getRandomMove(self):
        legalMoves = self.board.getAllMovesLegal()
        randomMove = random.choice(legalMoves)
        return randomMove

    def makeRandomMove(self):
        randomMove = self.getRandomMove()
        self.board.makeMove(randomMove)

    # The Roots
    def generateMoveTree(self):
        moveTree = []
        for move in self.board.getAllMovesLegal():
            moveTree.append(MoveNode(move, [], None))

        for node in moveTree:
            self.board.makeMove(node.move)
            self.populateNodeChildren(node)
            self.board.undoLastMove()
        return moveTree

    # get all the nodes populated
    def populateNodeChildren(self, node):
        node.point = self.board.getPointValueOfSide(self.side)
        node.getDepth()
        if node.depth == self.depth:
            return

        legalMoves = self.board.getAllMovesLegal()
        if not legalMoves:
            node.move.checkmate = True
            return
        
        for move in legalMoves:
            node.children.append(MoveNode(move, [], node))
            self.board.makeMove(move)
            # recursive call, the last one is the one just been appended
            self.populateNodeChildren(node.children[-1])
            self.board.undoLastMove()


    
if __name__ == "__main__":
    playSide = WHITE
    board = Board()
    print(board)
    ai = AI(board, playSide, 2)
    moveTree = ai.generateMoveTree()
    print(moveTree[0].children[0].point)