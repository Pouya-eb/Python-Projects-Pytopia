def is_happy(number: int) -> bool:
    """Check whether given number is happy or not

    :param number: The number to check
    :return: True if number is happy, False otherwise
    """
    seen_numbers = set()

    while (number != 1) and (number not in seen_numbers):
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    
    return (number == 1)


if __name__ == '__main__':
    assert is_happy(19)
    assert not is_happy(2)
    assert not is_happy(4)
    assert is_happy(44)

    print('All test cases pass')
