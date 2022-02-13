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


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    pattern_1(size, character)
