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

    def getBestMove(self):
        moveTree = self.generateMoveTree()
        bestMoves = self.bestMovesWithMoveTree(moveTree)
        randomBestMove = random.choice(bestMoves)
        return randomBestMove

    def bestMovesWithMoveTree(self, moveTree):
        bestMoveNodes = []
        for moveNode in moveTree:
            moveNode.point = self.getMaxPointOfNode(moveNode)
            if not bestMoveNodes:
                bestMoveNodes.append(moveNode)
            elif moveNode > bestMoveNodes[0]:
                bestMoveNodes = []
                bestMoveNodes.append(moveNode)
            elif moveNode == bestMoveNodes[0]:
                bestMoveNodes.append(moveNode)
        return [node.move for node in bestMoveNodes]

    def getMaxPointOfNode(self, node):
        if node.children:
            for child in node.children:
                child.point = self.getMaxPointOfNode(child)
            
            if node.children[0].depth % 2 == 1:
                return max(node.children).point
            else:
                # opponnet's turn
                # face the worst situation
                return min(node.children).point
        
        return node.point

    def makeBestMove(self):
        bestMove = self.getBestMove()
        self.board.makeMove(bestMove)
    
if __name__ == "__main__":
    playSide = WHITE
    board = Board()
    ai = AI(board, playSide, 2)
    ai.makeBestMove()
    print(board)
    print(board.movesMade)