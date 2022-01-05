# Find total number of Squares in a N*N chessboard

def squaresInChessBoard(n):
    return int(((n * (n + 1) / 2)* (2 * n + 1) / 3))

print(squaresInChessBoard(8))