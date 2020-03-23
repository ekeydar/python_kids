# WRITE THE FUNCTION add_signs, similar to the add_starts in the
# previous exercise
# add paramter sign with default *


def main():
    print(add_signs('hello', '='))
    assert add_signs('hello') == '*********\n* hello *\n*********'
    assert add_signs('a','+') == '+++++\n+ a +\n+++++'
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()