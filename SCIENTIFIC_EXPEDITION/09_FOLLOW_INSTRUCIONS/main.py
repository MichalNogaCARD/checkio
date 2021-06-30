from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    x: int = 0
    y: int = 0

    for instruction in instructions:
        if instruction == 'f':
            y += 1
        elif instruction == 'b':
            y -= 1
        elif instruction == 'l':
            x = -1
        elif instruction == 'r':
            x += 1

    return x, y


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
