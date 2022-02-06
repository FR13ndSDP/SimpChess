from tokenize import Special


class Move:
    def __init__(self, piece, newPos, pieceToCapture):
        self.notation = None
        self.check = False
        self.checkmate = False
        self.kingsideCastle = False
        self.queensideCastle = False
        self.promotion = False
        self.passant = False
        self.stalemate = False

        self.piece = piece
        self.oldPos = piece.position
        self.newPos = newPos
        self.pieceToCapture = pieceToCapture
        # For en passant and castling
        self.specialMovePiece = None
        # For castling
        self.rookMove = None

    def __str__(self):
        displayString = (
            "Old pos :" + str(self.oldPos) + " -- New pos : " + str(self.newPos)
        )
        if self.notation:
            displayString += " Notation : " + self.notation
        if self.passant:
            displayString = (
                "Old pos : "
                + str(self.oldPos)
                + " -- New pos : "
                + str(self.newPos)
                + " -- Pawn taken : "
                + str(self.specialMovePiece)
                + "PASSANT"
            )
        return displayString

    def __eq__(self, other):
        if (
            self.oldPos == other.oldPos
            and self.newPos == other.newPos
            and self.specialMovePiece == other.specialMovePiece
        ):
            if not self.specialMovePiece:
                return True
            if (
                self.specialMovePiece
                and self.specialMovePiece == other.specialMovePiece
            ):
                return True
            else:
                return False
        else:
            return False

    # Redefine __hash__ here to make the class can be put in a set or list
    def __hash__(self):
        return hash((self.oldPos, self.newPos))

    # Undo the move
    def reverse(self):
        return Move(self.piece, self.piece.position, pieceToCapture=self.pieceToCapture)
    
