from pattern_1 import pattern_1_alphabets as pattern_1
from pattern_2 import pattern_2_alphabets as pattern_2
from pattern_3 import pattern_3_alphabets as pattern_3
from pattern_4 import pattern_4_alphabets as pattern_4
from pattern_5 import pattern_5_alphabets as pattern_5
from pattern_6 import pattern_6_alphabets as pattern_6
from pattern_7 import pattern_7_alphabets as pattern_7

if __name__ == "__main__":
    size = int(input("Please select the pattern size(number of lines):"))
    while 1:
        try:
            select_pattern = int(input("select the pattern you want to print(there are 7):"))
            if select_pattern == 1:
                print("Pattern-1:")
                pattern_1(size)
            elif select_pattern == 2:
                print("Pattern-2:")
                pattern_2(size)
            elif select_pattern == 3:
                print("Pattern-3:")
                pattern_3(size)
            elif select_pattern == 4:
                print("Pattern-4:")
                pattern_4(size)
            elif select_pattern == 5:
                print("Pattern-5:")
                pattern_5(size)
            elif select_pattern == 6:
                print("Pattern-6:")
                pattern_6(size)
            elif select_pattern == 7:
                print("Pattern-7:")
                pattern_7(size)
            else:
                print("Bye! Bye!")
                break
        except ValueError:
            print('ValueError! Try Again')
