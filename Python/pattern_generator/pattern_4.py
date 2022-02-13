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


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_4(size, character)
