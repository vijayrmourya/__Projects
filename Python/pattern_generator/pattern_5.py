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


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_5(size, character)
