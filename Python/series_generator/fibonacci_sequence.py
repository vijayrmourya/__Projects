"""
What is Fibonacci Series? A series of numbers in which each number (Fibonacci number) is the sum of the two
preceding numbers, starting from 0 and 1, i.e., 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
"""


def fib_seq(length):
    """
    generates the fibonacci series of given length
    :param length: type: int | defines series length to be generated
    :return: type: List | generated list in a list data type or False on error
    """
    fib_list = []
    num1, num2 = 0, 1
    try:
        for i in range(1, length + 1):
            fib_list.append(num1)
            num1, num2 = num2, num1 + num2
        return fib_list
    except TypeError:
        print("An Error Occurred (TypeError)")
        return False
    except ValueError:
        print("An Error Occurred (ValueError)")
        return False


if __name__ == '__main__':
    while 1:
        A = int(input("Please tell the length of series :"))
        print(fib_seq(A))
        x = input("do you want another list:(y/n)")
        if x.lower() == 'n':
            break
