
board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

def isValidChessBoard(board):
    pieceCount = {'b':0, 'w':0}  # b: black , w: white
    pawnCount =  {'b':0, 'w':0}
    hasKing = {'b': False, 'w': False}
    letterAxis = ('a','b','c','d','e','f','g','h')
    pieceColor = ('b','w')
    pieceType = ('pawn','knight','bishop','rook','queen','king')
    # Moi nguoi choi chi co <= 16 piece

    for pos,i in board.items():
        # Kiem tra vi tri cua quan co, vi tri chi duoc tu 1a ->> 8h
        if int(pos[0]) >= 9:
            print('spaceError')
            return False
        if pos[1] not in letterAxis:
            print('letterAxis error')
            return False
        # check piece data
        if i != "":
            # ten cua quan co bat dau bang w hoac b
            if i[0] not in pieceColor:
                print('white or black error')
                return False
            thisPieceColor = i[0]
            pieceCount[thisPieceColor] += 1
            if pieceCount[thisPieceColor] >= 17:
                print('total piece error')
                return False
            #piece names must follow with 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
            thisPieceType = i[1:]
            if thisPieceType not in pieceType:
                print('piece type error')
                return False
            elif thisPieceType == 'pawn':
                pawnCount[thisPieceColor] += 1
                # moi nguoi choi chi co toi da 8 pawn
                if pawnCount[thisPieceColor] >= 9:
                    print('total pawn error')
                    return False
            elif thisPieceType == 'king':
                #one black king and one white king
                if hasKing[thisPieceColor] == True:
                    print('piece king error')
                hasKing[thisPieceColor] = True 

    if list(hasKing.values()) != [True,True]:
        print('error')
        return False
    return 'It\'s OK'



print(isValidChessBoard(board))

        