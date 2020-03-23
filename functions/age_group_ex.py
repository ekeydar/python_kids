def age_group(age):
    """
    return age group according to age
    """
    # WRITE YOUR CODE HERE

def main():
    assert age_group(1) == "BABY"
    assert age_group(2) == "BABY"
    assert age_group(3) == "KID"
    assert age_group(10) == "KID"
    assert age_group(11) == "TEEN"
    assert age_group(18) == "TEEN"
    assert age_group(19) == "YOUNG"
    assert age_group(30) == "YOUNG"
    assert age_group(31) == "ADULT"
    assert age_group(41) == "ADULT"
    assert age_group(59) == "ADULT"
    assert age_group(60) == "SENIOR"
    assert age_group(70) == "SENIOR"

    print('Everything OK, well done!')

if __name__ == '__main__':
    main()