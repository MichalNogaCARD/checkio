def frequency_sort(items):
    element_frequency: dict = dict()
    out: list = []

    for item in items:
        element_frequency[item] = items.count(item)

    ordered_dict = dict(sorted(element_frequency.items(), key=lambda x: x[1], reverse=True))

    for key, value in ordered_dict.items():
        for i in range(value):
            out.append(key)

    return out


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
