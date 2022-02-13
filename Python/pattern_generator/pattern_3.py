from pattern_1 import pattern_1 as p1
from pattern_2 import pattern_2 as p2


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
    p1(size3, character3)
    p2(size3 - 1, character3)


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_3(size, character)
