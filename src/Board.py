# coding:utf-8

from Bishop import Bishop
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
from Rook import Rook
from King import King
from Coordinate import Coordinate as C
from Move import Move
from termcolor import colored

WHITE = True
BLACK = False


class Board:
    def __init__(self, castleBoard=False, passant=False, promotion=False):
        self.pieces = []
        self.history = []
        self.points = 0
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False

        self.pieces.extend(
            [
                Rook(self, BLACK, C(0, 7)),
                Knight(self, BLACK, C(1, 7)),
                Bishop(self, BLACK, C(2, 7)),
                Queen(self, BLACK, C(3, 7)),
                King(self, BLACK, C(4, 7)),
                Bishop(self, BLACK, C(5, 7)),
                Knight(self, BLACK, C(6, 7)),
                Rook(self, BLACK, C(7, 7)),
            ]
        )
        for x in range(8):
            self.pieces.append(Pawn(self, BLACK, C(x, 6)))
            self.pieces.append(Pawn(self, WHITE, C(x, 1)))

        self.pieces.extend(
            [
                Rook(self, WHITE, C(0, 0)),
                Knight(self, WHITE, C(1, 0)),
                Bishop(self, WHITE, C(2, 0)),
                Queen(self, WHITE, C(3, 0)),
                King(self, WHITE, C(4, 0)),
                Bishop(self, WHITE, C(5, 0)),
                Knight(self, WHITE, C(6, 0)),
                Rook(self, WHITE, C(7, 0)),
            ]
        )

    def __str__(self):
        return self.wrapStringRep(self.makeStringRep(self.pieces))

    def makeStringRep(self, pieces):
        DISPLAY_LOOKUP = {
            "R": "♜",
            "N": "♞",
            "B": "♝",
            "K": "♚",
            "Q": "♛",
            "P": "♟",
        }

        stringRep = ""
        for y in range(7, -1, -1):
            for x in range(8):
                piece = None
                for p in pieces:
                    if p.position == C(x, y):
                        piece = p
                        break
                on_color = "on_cyan" if y % 2 == x % 2 else "on_yellow"
                pieceRep = colored("  ", on_color=on_color)
                if piece:
                    side = piece.side
                    color = "white" if side == WHITE else "grey"
                    pieceRep = colored(
                        DISPLAY_LOOKUP.get(piece.stringRep) + " ", color, on_color
                    )
                stringRep += pieceRep
            stringRep += "\n"
        return stringRep.rstrip()

    def wrapStringRep(self, stringRep):
        sRep = "\n".join(
            [
                "%d  %s" % (8 - r, s.rstrip())
                for r, s in enumerate(stringRep.split("\n"))
            ]
            + ["\n   a b c d e f g h"]
        ).rstrip()
        return sRep

    def getCurrentSide(self):
        return self.currentSide

    def pieceAtPosition(self, pos):
        for piece in self.pieces:
            if piece.position == pos:
                return piece

    def isValidPos(self, pos):
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return True
        else:
            return False

    def movePieceToPosition(self, piece, coord):
        piece.position = coord

    def getPositionOfPiece(self, piece):
        return piece.position

    def makeMove(self, move):
        self.history.append(move)
        pieceToMove = move.piece
        pieceToTake = move.pieceToCapture

        if move.promotion:
            self.pieces.remove(move.piece)
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                else:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)

            self.pieces.append(move.specialMovePiece)
            if move.piece.side == WHITE:
                self.points += move.specialMovePiece.value - 1
            else:
                self.points -= move.specialMovePiece.value - 1
        else:
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                else:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)
            self.movePieceToPosition(pieceToMove, move.newPos)

        pieceToMove.movesMade += 1
        self.movesMade += 1
        self.currentSide = not self.currentSide

    def getPointValueOfSide(self, side):
        points = 0
        for piece in self.pieces:
            if piece.side == side:
                points += piece.value
        return points

    def undoLastMove(self):
        lastMove = self.history.pop()
        pieceTaken = lastMove.pieceToCapture
        if lastMove.promotion:
            pawnPromoted = lastMove.piece
            promotedPiece = lastMove.specialMovePiece
            self.pieces.remove(promotedPiece)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                else:
                    self.points -= pieceTaken.value
                self.pieces.append(pieceTaken)
            self.pieces.append(pawnPromoted)
            if pawnPromoted.side == WHITE:
                self.points -= promotedPiece.value - 1
            else:
                self.points += promotedPiece.value - 1
            pawnPromoted.movesMade -= 1
        else:
            pieceToMoveBack = lastMove.piece
            self.movePieceToPosition(pieceToMoveBack, lastMove.oldPos)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                else:
                    self.points -= pieceTaken.value
                self.pieces.append(pieceTaken)
            pieceToMoveBack.movesMade -= 1

        self.currentSide = not self.currentSide

    # Don't aware of checkmate
    def getAllMovesUnfiltered(self):
        unfilteredMoves = []
        for piece in self.pieces:
            if piece.side == self.currentSide:
                for move in piece.getPossibleMoves():
                    unfilteredMoves.append(move)
        return unfilteredMoves

    def moveIsLegal(self, move):
        self.makeMove(move)
        for moveOpposite in self.getAllMovesUnfiltered():
            pieceToTake = moveOpposite.pieceToCapture
            if pieceToTake and pieceToTake.stringRep == "K":
                self.undoLastMove()
                return False
        self.undoLastMove()
        return True

    def getAllMovesLegal(self):
        unfilteredMoves = self.getAllMovesUnfiltered()
        legalMoves = []
        for move in unfilteredMoves:
            if self.moveIsLegal(move):
                legalMoves.append(move)
        return legalMoves

    def isCheckmate(self):
        if len(self.getAllMovesLegal()) == 0:
            return True
        return False