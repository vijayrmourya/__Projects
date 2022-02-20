"""
alphabets_&_ascii.py: module to get details of Alphabets and their ASCII values
"""
from pprint import pprint as pretty

__all__ = ['ascii_dictionary', 'capital_letters_ascii', 'small_letters_ascii']


def ascii_dictionary(upto):
    """
    ascii_dictionary creates a dictionary of all characters up to the int number provided
    :param
        upto: defines the upper limit of the dictionary elements
    :return:
        dictionary of all character and ASCII value pair
    """
    n = 0
    all_ascii = {}
    while n < upto + 1:
        if str(chr(n)) == '𖫭':
            n += 1
            continue
        else:
            all_ascii[str(chr(n))] = n
            n += 1
    return all_ascii


def capital_letters_ascii():
    """
    capital_letters_ascii creates a dictionary of all Capital letters
    :return: dictionary of all Capital letters
    """
    capital_start = 65
    cap_letters = {}
    while 1:
        cap_letters[str(chr(capital_start))] = capital_start
        capital_start += 1
        if chr(capital_start) == 'Z':
            cap_letters[str(chr(capital_start))] = capital_start
            break
    return cap_letters


def small_letters_ascii():
    """
    small_letters_ascii creates a dictionary of all Small letters
    :return: dictionary of all Small letters
    """
    small_start = 97
    sml_letters = {}
    while 1:
        sml_letters[str(chr(small_start))] = small_start
        small_start += 1
        if chr(small_start) == 'z':
            sml_letters[str(chr(small_start))] = small_start
            break
    return sml_letters


if __name__ == '__main__':
    print()
    print("These are ASCII letters")
    pretty(ascii_dictionary(int(input("select the ascii_dictionary range(int):"))))
    print("These are capital letters")
    pretty(capital_letters_ascii())
    print("These are small letters")
    pretty(small_letters_ascii())
