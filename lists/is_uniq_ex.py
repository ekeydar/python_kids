def is_uniq_list(lst):
    """
    return True if all items in list are the same
    """
    # your code here


def main():
    assert is_uniq_list(["aaa", "bbb", "ccc"]) is False
    assert is_uniq_list(["aaa", "bbb", "aaa"]) is False
    assert is_uniq_list(["ccc", "ccc", "ccc"]) is True
    assert is_uniq_list(["bbb", "bb"]) is False
    assert is_uniq_list(["xxx"]) is True
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()
