import math


def split_list(items: list) -> list:
    full_length = int(len(items))
    half_length = int(full_length / 2)

    return [items[0:half_length], items[half_length:full_length]] if full_length % 2 == 0 else [
        items[0:math.floor(half_length) + 1], items[math.floor(half_length) + 1:full_length]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
