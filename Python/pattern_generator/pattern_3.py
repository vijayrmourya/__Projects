from pattern_1 import *
from pattern_2 import *

__all__ = ['pattern_3', 'pattern_3_alphabets', 'pattern_3_numbers']


def pattern_3(size3, character3):
    """
    %
    %%
    %%%
    %%%%
    %%%%%
    %%%%
    %%%
    %%
    %
    :param size3: pattern size (lines)
    :param character3: character to be printed in pattern
    :return:
    """
    pattern_1(size3, character3)
    pattern_2(size3 - 1, character3)


def pattern_3_alphabets(size3):
    """
    A
    AB
    ABC
    ABCD
    ABC
    AB
    A
    :param size3: pattern size (lines)
    :return:
    """
    pattern_1_alphabets(size3)
    pattern_2_alphabets(size3 - 1)


def pattern_3_numbers(size3):
    """
    0
    01
    012
    0123
    01234
    0123
    012
    01
    0
    :param size3: pattern size (lines)
    :return:
    """
    pattern_1_numbers(size3)
    pattern_2_numbers(size3 - 1)


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_3(size, character)
    pattern_3_alphabets(size)
    pattern_3_numbers(size)
