from pattern_4 import pattern_4 as pattern_4


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


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_6(size, character)
