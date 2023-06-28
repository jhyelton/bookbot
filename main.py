import os

def main():
    with open(os.path.join(os.path.dirname(__file__),"books/frankenstein.txt")) as f:
        file_contents = f.read()
        print(file_contents)


if __name__ == '__main__':
    main()