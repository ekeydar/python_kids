import math

# WRITE THE CODE HERE
# copy the code of get_circle_area from the previous exercise
# and write new function sum_circles_areas

def get_circle_area(r):
    """
    return area of circle
    """
    return math.pi * r * r


def sum_circles_areas(r1, r2, r3):
    """
    return sum of areas of circles
    """
    return get_circle_area(r1) + get_circle_area(r2) + get_circle_area(r3)



def main():
    assert 4398 < sum_circles_areas(10, 20, 30) < 4399
    assert 486.9 < sum_circles_areas(5, 7, 9) < 487
    print('Everything OK, well done!')


if __name__ == '__main__':
    main()