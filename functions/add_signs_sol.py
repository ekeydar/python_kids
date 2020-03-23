def add_signs(text, sign = '*'):
    """ return text wrapped in sign """
    len_line = len(text) + 4
    signs = sign * len_line
    text_line = sign + ' ' + text + ' ' + sign
    return signs + '\n' + text_line + '\n' + signs


def main():
    print(add_signs('hello', '='))
    assert add_signs('hello') == '*********\n* hello *\n*********'
    assert add_signs('a','+') == '+++++\n+ a +\n+++++'
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()