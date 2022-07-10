from typing import List, Tuple
import math


def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    groups = len(circles)

    for circle in circles:
        i = circles.index(circle)
        x1 = circle[0]
        y1 = circle[1]
        r1 = circle[2]
        while i < len(circles) - 1:
            if groups > 1:
                x2 = circles[i + 1][0]
                y2 = circles[i + 1][1]
                r2 = circles[i + 1][2]
                distance = get_distance(x1, y1, x2, y2)
                if distance < (r1 + r2):
                    if distance + min(r1, r2) > max(r1, r2):
                        groups -= 1
            i += 1
    return groups


#
#
# def count_chains(circles: List[Tuple[int, int, int]]) -> int:
#     groups = len(circles)
#     for circle in circles:
#         i = circles.index(circle)
#         while i < len(circles) - 1:
#             if groups > 1:
#                 distance = get_distance(circle[0], circles[i + 1][0], circle[1], circles[i + 1][1])
#                 if distance < (circle[2] + circles[i + 1][2]):
#                     if distance + min(circle[2], circles[i + 1][2]) >= max(circle[2], circles[i + 1][2]):
#                         groups -= 1
#             i += 1
#     return groups


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
