'''
A simple password generator.
'''

from random import choice

def load(filename):
    ''' Load characters from file '''
    try:
        with open(filename, 'r') as inFile:
            content = [l.strip() for l in inFile.readlines()]
        return content

    except IOError:
        print("Could not read file:", filename)


def parse(content):
    ''' Parse the content of file '''
    char_str = ''

    for l in content:
        if l and l[0] != '#':
            char_str += l

    return char_str


def generate(char_str, length):
    ''' Generate a password '''
    password = ''

    for i in range(length):
        char = choice(char_str)
        password += char

    return password


def main():
    ''' Main '''
    filename = 'characters.txt'

    content = load(filename)
    char_str = parse(content)
    length = int(input('Length of the password? '))

    password = generate(char_str, length)
    print('New Password:', password)


if __name__ == '__main__':
    main()
