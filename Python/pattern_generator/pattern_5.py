__all__ = ['pattern_5', 'pattern_5_alphabets', 'pattern_5_numbers']


def pattern_5(size5, character5):
    """
         %
        %%
       %%%
      %%%%
     %%%%%
    :param size5: pattern size (lines)
    :param character5: character to be printed in pattern
    :return:
    """
    for i in range(size5, 0, -1):
        for j in range(i, 0, -1):
            print(" ", end='')
        for k in range(i, size5 + 1):
            print(character5, end='')
        print(end="\n")


def pattern_5_alphabets(size5):
    """
         A
        AB
       ABC
      ABCD
     ABCDE
    :param size5: pattern size (lines)
    :return:
    """
    alphabet = 65
    for i in range(size5, 0, -1):
        for j in range(i, 0, -1):
            print(" ", end='')
        for k in range(i, size5 + 1):
            print(chr(alphabet), end='')
            if chr(alphabet) == 'Z':
                alphabet = 65
            else:
                alphabet += 1
        print(end="\n")
        alphabet = 65


def pattern_5_numbers(size5):
    """
         0
        01
       012
      0123
     01234
    :param size5: pattern size (lines)
    :return:
    """
    number = 0
    for i in range(size5, 0, -1):
        for j in range(i, 0, -1):
            print(" ", end='')
        for k in range(i, size5 + 1):
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
    pattern_5(size, character)
    pattern_5_alphabets(size)
    pattern_5_numbers(size)

