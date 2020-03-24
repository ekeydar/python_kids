def is_uniq_list(lst):
    """
    return True if all items in list are the same
    """
    if len(lst) <= 1:
        return True
    sorted_lst = sorted(lst)
    return sorted_lst[0] == sorted_lst[-1]


def main():
    assert is_uniq_list(["aaa", "bbb", "ccc"]) is False
    assert is_uniq_list(["aaa", "bbb", "aaa"]) is False
    assert is_uniq_list(["ccc", "ccc", "ccc"]) is True
    assert is_uniq_list(["bbb", "bb"]) is False
    assert is_uniq_list(["xxx"]) is True
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()
