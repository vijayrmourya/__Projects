__all__ = ['pattern_4', 'pattern_4_alphabets', 'pattern_4_numbers']


def pattern_4(size4, character4):
    """
     %%%%%
      %%%%
       %%%
        %%
         %
    :param size4: pattern size (lines)
    :param character4: character to be printed in pattern
    :return:
    """
    for i in range(1, size4 + 1):
        for j in range(0, i):
            print(" ", end='')
        for k in range(i, size4 + 1):
            print(character4, end='')
        print(end="\n")


def pattern_4_alphabets(size4):
    """
     ABCDE
      ABCD
       ABC
        AB
         A
    :param size4: pattern size (lines)
    :return:
    """
    alphabet = 65
    for i in range(1, size4 + 1):
        for j in range(0, i):
            print(" ", end='')
        for k in range(i, size4 + 1):
            print(chr(alphabet), end='')
            if chr(alphabet) == 'Z':
                alphabet = 65
            else:
                alphabet += 1
        print(end="\n")
        alphabet = 65


def pattern_4_numbers(size4):
    """
     01234
      0123
       012
        01
         0
    :param size4: pattern size (lines)
    :return:
    """
    number = 0
    for i in range(1, size4 + 1):
        for j in range(0, i):
            print(" ", end='')
        for k in range(i, size4 + 1):
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
    pattern_4(size, character)
    pattern_4_alphabets(size)
    pattern_4_numbers(size)
