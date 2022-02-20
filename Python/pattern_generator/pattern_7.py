__all__ = ['pattern_7', 'pattern_7_alphabets', 'pattern_7_numbers']


def pattern_7(size7, character7):
    """
        *
       ***
      *****
     *******
    *********
    :param size7: number if lines in pyrameter
    :param character7: character to be printed as pyramid
    :return:
    """
    for i in range(size7):
        space_printer = 0
        while space_printer < size7 - i:
            print(' ', end='')
            space_printer += 1
        char_printer = i - 1
        while char_printer < i * 3:
            print(character7, end='')
            char_printer += 1
        print(end="\n")


def pattern_7_alphabets(size7):
    alphabet = 65
    for i in range(size7):
        space_printer = 0
        while space_printer < size7 - i:
            print(' ', end='')
            space_printer += 1
        char_printer = i - 1
        while char_printer < i * 3:
            print(chr(alphabet), end='')
            char_printer += 1
            if chr(alphabet) == 'Z':
                alphabet = 65
            else:
                alphabet += 1
        print(end="\n")
        alphabet = 65


def pattern_7_numbers(size7):
    number = 0
    for i in range(size7):
        space_printer = 0
        while space_printer < size7 - i:
            print(' ', end='')
            space_printer += 1
        char_printer = i - 1
        while char_printer < i * 3:
            print(number, end='')
            char_printer += 1
            if number == 9:
                number = 0
            else:
                number += 1
        print(end="\n")
        number = 0


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_7(size, character)
    pattern_7_alphabets(size)
    pattern_7_numbers(size)
