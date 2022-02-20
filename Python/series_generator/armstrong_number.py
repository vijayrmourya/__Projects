"""
What is Armstrong Number?
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.

For example, 153 is an armstrong number

153 = 1^3 + 5^3 + 3^3
153 = 1 + 125 + 27
153 = 153
"""


def armstrong_number(check_number):
    """
    this function checks if given number is armstrong or not
    :param check_number: (type= int) number to be checked if armstrong or not
    :return: boolean based on result
    """
    try:
        sum = 0
        num = str(check_number)
        for i in num:
            sum += int(i) ** 3
        if sum == check_number:
            return True
        else:
            return False
    except ValueError:
        print("An Error Occurred (ValueError)")
        return False
    except TypeError:
        print("An Error Occurred (TypeError)")
        return False


if __name__ == '__main__':
    while 1:
        try:
            number = int(input("the number to be checked as Armstrong:"))
            if armstrong_number(number):
                print(f"{number} is a Armstrong number")
            else:
                print(f"{number} is not a Armstrong number")
        except TypeError:
            print("An error occurred please try again")
        except ValueError:
            print("An error occurred please try again")
