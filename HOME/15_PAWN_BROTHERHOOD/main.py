def safe_pawns(pawns: set) -> int:
    output: set = set()

    for pawn_coord in pawns:
        left_safe_position: str = chr(ord(pawn_coord[0]) - 1) + str(int(pawn_coord[1]) + 1)
        right_safe_position: str = chr(ord(pawn_coord[0]) + 1) + str(int(pawn_coord[1]) + 1)
        output.add(left_safe_position) if left_safe_position in pawns else False
        output.add(right_safe_position) if right_safe_position in pawns else False

    return len(output)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
