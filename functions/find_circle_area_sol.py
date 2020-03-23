import math


def get_circle_area(r):
    """
    return area of circle
    """
    return math.pi * r * r


def main():
    assert 3.14 < get_circle_area(1) < 3.15
    assert 12.56 < get_circle_area(2) < 12.57
    assert 28.2 < get_circle_area(3) < 28.3
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()