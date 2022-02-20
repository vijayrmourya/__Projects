__all__ = ['pattern_2', 'pattern_2_alphabets', 'pattern_2_numbers']


def pattern_2(size2, character2):
    """
    %%%%%
    %%%%
    %%%
    %%
    %
    :param size2: pattern size (lines)
    :param character2: character to be printed in pattern
    :return:
    """
    for i in range(size2, 0, -1):
        for j in range(i, 0, -1):
            print(character2, end='')
        print(end="\n")
    return 0


def pattern_2_alphabets(size2):
    """
    ABCDE
    ABCD
    ABC
    AB
    A
    :param size2:
    :return:
    """
    alphabet = 65
    for i in range(size2, 0, -1):
        for j in range(i, 0, -1):
            print(chr(alphabet), end='')
            if chr(alphabet) == 'Z':
                alphabet = 65
            else:
                alphabet += 1
        print(end="\n")
        alphabet = 65
    return 0


def pattern_2_numbers(size2):
    """
    0
    01
    012
    0123
    01234
    :param size2:
    :return:
    """
    numbers = 0
    for i in range(size2, 0, -1):
        for j in range(i, 0, -1):
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
    pattern_2(size, character)
    pattern_2_alphabets(size)
    pattern_2_numbers(size)
