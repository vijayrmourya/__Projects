from pattern_4 import *

__all__ = ['pattern_6', 'pattern_6_alphabets', 'pattern_6_numbers']


def pattern_6(size6, character6):
    """
     %%%%%
      %%%%
       %%%
        %%
         %
        %%
       %%%
      %%%%
     %%%%%
    :param size6: pattern size (lines)
    :param character6: character to be printed in pattern
    :return:
    """
    pattern_4(size6, character6)
    for i in range(size6, 1, -1):
        for j in range(i, 1, -1):
            print(" ", end='')
        for k in range(i - 1, size6 + 1):
            print(character6, end='')
        print(end="\n")


def pattern_6_alphabets(size6):
    """
     ABCDE
      ABCD
       ABC
        AB
         A
        AB
       ABC
      ABCD
     ABCDE
    :param size6: pattern size (lines)
    :return:
    """
    alphabet = 65
    pattern_4_alphabets(size6)
    for i in range(size6, 1, -1):
        for j in range(i, 1, -1):
            print(" ", end='')
        for k in range(i - 1, size6 + 1):
            print(chr(alphabet), end='')
            if chr(alphabet) == 'Z':
                alphabet = 65
            else:
                alphabet += 1
        print(end="\n")
        alphabet = 65


def pattern_6_numbers(size6):
    """
     01234
      0123
       012
        01
         0
        01
       012
      0123
     01234
    :param size6: pattern size (lines)
    :return:
    """
    number = 0
    pattern_4_numbers(size6)
    for i in range(size6, 1, -1):
        for j in range(i, 1, -1):
            print(" ", end='')
        for k in range(i - 1, size6 + 1):
            print(number, end='')
            if number == 9:
                number = 0
            else:
                number += 1
        print(end="\n")
        number = 0


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_6(size, character)
    pattern_6_alphabets(size)
    pattern_6_numbers(size)
