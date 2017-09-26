"""
generate a random string
"""
#-*- coding UTF-8 -*-
import random


def generate_string(length, string_type=0):
    """
    :param length: the length of the string that you want to generate
    :param string_type: the type of the string, 0 means random, 1 means UPPER, 2 means lower
    :return: a total random string
    """

    result = [""]
    source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if string_type == 1:
        start = 26
        end = 51
    elif string_type == 2:
        start = 0
        end = 25
    else:
        start = 0
        end = 51

    while len(result) <= length:
        result.append(source[random.randrange(start, end)])

    return "".join(result)

if __name__ == '__main__':
    print(generate_string(50))
    print(generate_string(50, 1))
    print(generate_string(50, 2))
