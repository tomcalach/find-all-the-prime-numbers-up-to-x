def find_all_prime_upto_x(x):
    """
    the function finds all the prime numbers up to the int x
    :param x: int
    :return: list of ints
    """
    prime_numbers = [2]
    for integer in range(3, x+1, 2):

        check = 3
        while check <= integer**0.5:
            if integer % check == 0:
                break
            check += 2

        if check > integer**0.5:
            prime_numbers.append(integer)

    return prime_numbers

