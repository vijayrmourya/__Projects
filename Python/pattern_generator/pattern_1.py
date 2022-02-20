__all__ = ['pattern_1', 'pattern_1_alphabets', 'pattern_1_numbers']


def pattern_1(size1, character1):
    """
    %
    %%
    %%%
    %%%%
    %%%%%
    :param size1: pattern size (lines)
    :param character1: character to be printed in pattern
    :return:
    """
    for i in range(1, size1 + 1):
        for j in range(0, i):
            print(character1, end='')
        print(end="\n")
    return 0


def pattern_1_alphabets(size1):
    """
    A
    AB
    ABC
    ABCD
    ABCDE
    :param size1:
    :return:
    """
    alphabet = 65
    for i in range(1, size1 + 1):
        for j in range(0, i):
            print(chr(alphabet), end='')
            if chr(alphabet) == 'Z':
                alphabet = 65
            else:
                alphabet += 1
        print(end="\n")
        alphabet = 65
    return 0


def pattern_1_numbers(size1):
    """
    0
    01
    012
    0123
    01234
    :param size1:
    :return:
    """
    numbers = 0
    for i in range(1, size1 + 1):
        for j in range(0, i):
            print(numbers, end='')
            if numbers == 9:
                numbers = 0
            else:
                numbers += 1
        print(end="\n")
        numbers = 0
    return 0


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_1(size, character)
    pattern_1_alphabets(size)
    pattern_1_numbers(size)
