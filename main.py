import os

def main():
    with open(os.path.join(os.path.dirname(__file__),"books/frankenstein.txt")) as f:
        file_contents = f.read()
        print(word_count(file_contents))


def word_count(text):
    return len(text.split())

if __name__ == '__main__':
    main()