import itertools


def long_repeat(line: str) -> int:
    return 0 if len(line) == 0 else max([len(list(group)) for character, group in itertools.groupby(line)])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
