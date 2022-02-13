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


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_2(size, character)