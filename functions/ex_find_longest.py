def find_longest(s1, s2):
    """
    returns longest string, if equal length return s1
    """
    if len(s1) >= len(s2):
        return s1
    else:
        return s2


def main():
    assert find_longest("abc", "aa") == "abc"
    assert find_longest("aa", "abc") == "abc"
    assert find_longest("zz", "") == "zz"
    assert find_longest("aaa", "zz") == "aaa"
    assert find_longest("aaa", "bbb") == "aaa"
    print('Everything OK, well done!')

if __name__ == '__main__':
    main()
