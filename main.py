import os

def main():
    with open(os.path.join(os.path.dirname(__file__),"books/frankenstein.txt")) as f:
        file_contents = f.read()
        print(char_count(file_contents))


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