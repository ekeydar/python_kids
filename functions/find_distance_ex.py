def find_distance(num1, num2):
    """
    return distance between num1 and num2
    """
    # your code here


def main():
    assert find_distance(5, 3) == 2
    assert find_distance(3, 5) == 2
    assert find_distance(7, 7) == 0
    assert find_distance(7.5, 7) == 0.5
    assert find_distance(7.5, 7.5) == 0
    assert find_distance(7, 8.5) == 1.5
    print('Everything OK, well done!')

if __name__ == '__main__':
    main()