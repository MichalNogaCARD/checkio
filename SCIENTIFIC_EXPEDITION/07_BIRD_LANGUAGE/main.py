def translate(text: str) -> str:
    idx: int = 0
    result: list = []

    while idx < len(text):
        result.append(text[idx])

        if text[idx] in 'aeouiy':
            idx += 3
        elif text[idx].isspace():
            idx += 1
        else:
            idx += 2

    return ''.join(result)


if __name__ == '__main__':
    print("Example:")
    print(translate('hieeelalaooo'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate('hieeelalaooo') == 'hello'
    assert translate('hoooowe yyyooouuu duoooiiine') == 'how you doin'
    assert translate('aaa bo cy da eee fe') == 'a b c d e f'
    assert translate('sooooso aaaaaaaaa') == 'sos aaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
