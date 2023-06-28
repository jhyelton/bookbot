import os

def main():
    with open(os.path.join(os.path.dirname(__file__),"books/frankenstein.txt")) as f:
        file_contents = f.read()
        print(report(file_contents))

def report(text):
    report = [
        "--- Begin report of books/frankenstein.txt ---"
        "\n"
        f"{word_count(text)} words found in the document"
        "\n"
    ]
    char_map = char_count(text)
    chars = list(char_map.keys())
    chars.sort()
    for char in chars:
        if char.isalpha():
            report.append(f"The {char} character was found {char_map[char]} times")
    report.append("--- End report ---")
    return "\n".join(report)


def word_count(text):
    return len(text.split())

def char_count(text):
    char_map = {}
    for char in text.lower():
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map

if __name__ == '__main__':
    main()