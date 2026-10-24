import chess

def get_square(row, col):
    return chess.square(col, 7 - row)

result = get_square(7, 0)

print(result)
print(type(result))