from collections import Counter
import re


def checkio(text: str) -> str:
    frequencies = Counter(list(re.sub('[^a-z]', '', text.lower())))
    output: list = [entry for entry in frequencies.most_common() if entry[1] == frequencies.most_common(1)[0][1]]
    output_sorted: list = [element[0] for element in output]
    output_sorted.sort()
    return output_sorted[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("Lorem ipsum dolor sit amet") == "m"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
