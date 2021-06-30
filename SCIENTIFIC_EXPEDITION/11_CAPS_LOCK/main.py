def caps_lock(text: str) -> str:
    caps_lock_on: bool = False
    idx: int = 0
    output_text: list = []

    while idx < len(text):
        if text[idx] == 'a':
            caps_lock_on = not caps_lock_on
        else:
            if text[idx].isupper():
                output_text.append(text[idx])
            else:
                output_text.append(text[idx].upper() if caps_lock_on else text[idx].lower())
        idx += 1

    return text[0] + ''.join(output_text[1:])


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
