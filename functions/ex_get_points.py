def get_points(goals1, goals2):
    """
    returns score of football game
    """
    if goals1  > goals2:
        return 3, 0
    if goals2 > goals1:
        return 0, 3
    return 1, 1


def main():
    assert get_points(2, 2) == (1, 1)
    assert get_points(1, 0) == (3, 0)
    assert get_points(1, 4) == (0, 3)
    print('Everything OK, well done!')

if __name__ == '__main__':
    main()
