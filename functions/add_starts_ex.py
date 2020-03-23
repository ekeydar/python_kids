def add_starts(text):
    """ return text wrapped in * """
    # WRITE YOUR CODE HERE

def main():
    print(add_starts('hello'))
    assert add_starts('hello') == '*********\n* hello *\n*********'
    assert add_starts('a') == '*****\n* a *\n*****'
    print('Everything OK, well done!')

if __name__ == '__main__':
    main()