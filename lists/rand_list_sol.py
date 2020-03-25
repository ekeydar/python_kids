import random


def rand_list3():
    """
    return list of 3 random items between 1 to 10 (include 1 and include 10)
    """
    return [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]


def main():
    assert len(rand_list3()) == 3, 'list should be in size 3'
    items = set()
    for x in range(1000):
        items |= set(rand_list3())
    assert items == set(range(1, 11)), 'Probably something wrong with your call to random.randint'
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()
