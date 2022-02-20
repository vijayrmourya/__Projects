"""
number_system_conversions is code to convert any number from one number system to another
from binary to octal, decimal and hexadecimal or the other way around for all number systems

user needs to provide a number in any one number system for ex., user provides 110011 in binary will be given output
in octal, decimal and hexadecimal
"""
import math

__all__ = ['is_binary', 'is_octal', 'is_decimal', 'is_hex', 'binary_to_decimal', 'octal_to_decimal',
           'hexadecimal_to_decimal', 'decimal_to_binary', 'octal_to_binary', 'hex_to_binary', 'decimal_to_octal',
           'binary_to_octal', 'hexadecimal_to_octal', 'decimal_to_hexadecimal', 'binary_to_hexadecimal',
           'octal_to_hexadecimal', 'convertor']


def is_binary(number_2):
    """
    to check if give number is binary or not
    :param number_2: (type=str)(ex. '1100') user provided number to check if It's binary or not
    :return: bool based on result if number is binary or not
    """
    try:
        for i in number_2:
            if int(i) == 1 or int(i) == 0:
                continue
            else:
                return False
        return True
    except ValueError:
        print("An Error occurred! Invalid number")
        return False
    except TypeError:
        print("An Error occurred! Invalid number")
        return False


def is_octal(number_8):
    """
    to check if give number is octal or not
    :param number_8: (type=str)(ex. '746') user provided number to check if It's octal or not
    :return: bool based on result if number is octal or not
    """
    try:
        for i in number_8:
            if 0 <= int(i) <= 7:
                continue
            else:
                return False
        return True
    except ValueError:
        print("An Error occurred! Invalid number")
        return False
    except TypeError:
        print("An Error occurred! Invalid number")
        return False


def is_decimal(number_10):
    """
    to check if give number is decimal or not
    :param number_10: (type=int)(ex. 956) user provided number to check if It's decimal or not
    :return: bool based on result if number is decimal or not
    """
    try:
        if number_10 % 1 == 0:
            return True
        else:
            return False
    except ValueError:
        print("An Error occurred! Invalid number")
        return False
    except TypeError:
        print("An Error occurred! Invalid number")
        return False


def is_hex(number_16):
    """
    to check if give number is hexadecimal or not
    :param number_16: (type=str) (ex. 'FF001') user provided number to check if It's hexadecimal or not
    :return: bool based on result if number is hex or not
    """
    try:
        for i in number_16:
            if i.upper() == 'A' or i.upper() == 'B' or i.upper() == 'C' or i.upper() == 'D' or i.upper() == 'E' or i.upper() == 'F':
                continue
            elif 0 < int(i) < 10:
                continue
            else:
                return False
        return True
    except ValueError:
        print("An Error occurred! Invalid number")
        return False
    except TypeError:
        print("An Error occurred! Invalid number")
        return False


def binary_to_decimal(number_2_10):
    """
    To convert given number from binary to decimal
    :param number_2_10: (type=str)(ex. '1100') user provided number to be converted from binary to decimal
    :return: type(int) decimal number (as a module returns either decimal number or false)
    """
    if __name__ != '__main__':
        if is_binary(number_2_10):
            decimal_number_2_10 = 0
            power_2_10 = 0
            for i in number_2_10[::-1]:
                decimal_number_2_10 = decimal_number_2_10 + int(i) * math.pow(2, power_2_10)
                power_2_10 += 1
            return decimal_number_2_10
        else:
            return False
    else:
        decimal_number_2_10 = 0
        power_2_10 = 0
        for i in number_2_10[::-1]:
            decimal_number_2_10 = decimal_number_2_10 + int(i) * math.pow(2, power_2_10)
            power_2_10 += 1
        return decimal_number_2_10


def octal_to_decimal(number_8_10):
    """
    To convert given number from octal to decimal
    :param number_8_10: (type=str) user provided number to be converted from octal to decimal
    :return: type(int) decimal number (as a module returns either decimal number or false)
    """
    if __name__ != '__main__':
        if is_octal(number_8_10):
            decimal_number_8_10 = 0
            power_8_10 = 0
            for i in number_8_10[::-1]:
                decimal_number_8_10 = decimal_number_8_10 + int(i) * math.pow(8, power_8_10)
                power_8_10 += 1
            return decimal_number_8_10
        else:
            return False
    else:
        decimal_number_8_10 = 0
        power_8_10 = 0
        for i in number_8_10[::-1]:
            decimal_number_8_10 = decimal_number_8_10 + int(i) * math.pow(8, power_8_10)
            power_8_10 += 1
        return decimal_number_8_10


def hexadecimal_to_decimal(number_16_10):
    """
    To convert given number from hexadecimal to decimal
    :param number_16_10: (type=str) user provided number to be converted from hexadecimal to decimal
    :return: type(int) decimal number (as a module returns either decimal number or false)
    """
    if __name__ != '__main__':
        if is_hex(number_16_10):
            decimal_number_16_10 = 0
            power_16_10 = 0
            for i in number_16_10[::-1]:
                if i.upper() == 'A':
                    decimal_number_16_10 += 10 * math.pow(16, power_16_10)
                    power_16_10 += 1
                elif i.upper() == 'B':
                    decimal_number_16_10 += 11 * math.pow(16, power_16_10)
                    power_16_10 += 1
                elif i.upper() == 'C':
                    decimal_number_16_10 += 12 * math.pow(16, power_16_10)
                    power_16_10 += 1
                elif i.upper() == 'D':
                    decimal_number_16_10 += 13 * math.pow(16, power_16_10)
                    power_16_10 += 1
                elif i.upper() == 'E':
                    decimal_number_16_10 += 14 * math.pow(16, power_16_10)
                    power_16_10 += 1
                elif i.upper() == 'F':
                    decimal_number_16_10 += 15 * math.pow(16, power_16_10)
                    power_16_10 += 1
                else:
                    decimal_number_16_10 += int(i) * math.pow(16, power_16_10)
                    power_16_10 += 1
            return decimal_number_16_10
        else:
            return False
    else:
        decimal_number_16_10 = 0
        power_16_10 = 0
        for i in number_16_10[::-1]:
            if i.upper() == 'A':
                decimal_number_16_10 += 10 * math.pow(16, power_16_10)
                power_16_10 += 1
            elif i.upper() == 'B':
                decimal_number_16_10 += 11 * math.pow(16, power_16_10)
                power_16_10 += 1
            elif i.upper() == 'C':
                decimal_number_16_10 += 12 * math.pow(16, power_16_10)
                power_16_10 += 1
            elif i.upper() == 'D':
                decimal_number_16_10 += 13 * math.pow(16, power_16_10)
                power_16_10 += 1
            elif i.upper() == 'E':
                decimal_number_16_10 += 14 * math.pow(16, power_16_10)
                power_16_10 += 1
            elif i.upper() == 'F':
                decimal_number_16_10 += 15 * math.pow(16, power_16_10)
                power_16_10 += 1
            else:
                decimal_number_16_10 += int(i) * math.pow(16, power_16_10)
                power_16_10 += 1
        return decimal_number_16_10


def decimal_to_binary(number_10_2):
    """
    To convert given number from decimal to binary
    :param number_10_2: (type=int) user provided number to be converted from decimal to binary
    :return: (type=str) binary number (as a module returns either binary number or false)
    """
    if __name__ != '__main__':
        if is_decimal(number_10_2):
            binary_number_10_2 = ''
            divisor_10_2 = 2
            while number_10_2 > 0:
                binary_number_10_2 = str(number_10_2 % divisor_10_2) + binary_number_10_2
                number_10_2 = int(number_10_2 // 2)
                if number_10_2 == 1:
                    binary_number_10_2 = str(number_10_2) + binary_number_10_2
                    number_10_2 = 0
            return binary_number_10_2
        else:
            return False
    else:
        binary_number_10_2 = ''
        divisor_10_2 = 2
        while number_10_2 > 0:
            binary_number_10_2 = str(number_10_2 % divisor_10_2) + binary_number_10_2
            number_10_2 = int(number_10_2 // 2)
            if number_10_2 == 1:
                binary_number_10_2 = str(number_10_2) + binary_number_10_2
                number_10_2 = 0
        return binary_number_10_2


def octal_to_binary(number_8_2):
    """
    To convert given number from octal to binary
    :param number_8_2: (type=str) user provided number to be converted from octal to binary
    :return: (type=str) binary number (as a module returns either binary number or false)
    """
    if __name__ != '__main__':
        if is_octal(number_8_2):
            decimal_number = octal_to_decimal(number_8_2)
            return decimal_to_binary(decimal_number)
        else:
            return False
    else:
        decimal_number = octal_to_decimal(number_8_2)
        return decimal_to_binary(decimal_number)


def hex_to_binary(number_16_2):
    """
    To convert given number from hexadecimal to binary
    :param number_16_2: (type=str) user provided number to be converted from hex to binary
    :return: (type=str) binary number (as a module returns either binary number or false)
    """
    if __name__ != '__main__':
        if is_hex(number_16_2):
            decimal_number = hexadecimal_to_decimal(number_16_2)
            return decimal_to_binary(decimal_number)
        else:
            return False
    else:
        decimal_number = hexadecimal_to_decimal(number_16_2)
        return decimal_to_binary(decimal_number)


def decimal_to_octal(number_10_8):
    """
    To convert given number from decimal to octal
    :param number_10_8: (type=int) user provided number to be converted to binary from decimal
    :return: (type=str) octal number (as a module returns either octal number or false)
    """
    if __name__ != '__main__':
        if is_decimal(number_10_8):
            octal_number_10_8 = ""
            number_10_8 = int(number_10_8)
            if number_10_8 < 8:
                return number_10_8
            else:
                while number_10_8 > 8:
                    right, left = math.modf(number_10_8 / 8)
                    number_10_8 = left
                    octal_number_10_8 = str(int(right * 8)) + octal_number_10_8
                right, left = math.modf(number_10_8 / 8)
                octal_number_10_8 = str(int(right * 8)) + octal_number_10_8
            return octal_number_10_8
        else:
            return False
    else:
        octal_number_10_8 = ""
        number_10_8 = int(number_10_8)
        if number_10_8 < 8:
            return number_10_8
        else:
            while number_10_8 > 8:
                right, left = math.modf(number_10_8 / 8)
                number_10_8 = left
                octal_number_10_8 = str(int(right * 8)) + octal_number_10_8
            right, left = math.modf(number_10_8 / 8)
            octal_number_10_8 = str(int(right * 8)) + octal_number_10_8
        return octal_number_10_8


def binary_to_octal(number_2_8):
    """
    To convert given number from binary to octal
    :param number_2_8: (type=str) user provided number to be converted from binary to octal
    :return: (type=str) octal number (as a module returns either octal number or false)
    """
    if __name__ != '__main__':
        if is_decimal(number_2_8):
            decimal_number = binary_to_decimal(number_2_8)
            return decimal_to_octal(decimal_number)
        else:
            return False
    else:
        decimal_number = binary_to_decimal(number_2_8)
        return decimal_to_octal(decimal_number)


def hexadecimal_to_octal(number_16_8):
    """
    To convert given number from hexadecimal to octal
    :param number_16_8: (type=str) user provided number to be converted from hexadecimal to octal
    :return: (type=str) octal number (as a module returns either octal number or false)
    """
    if __name__ != '__main__':
        if is_hex(number_16_8):
            decimal_number = hexadecimal_to_decimal(number_16_8)
            return decimal_to_octal(decimal_number)
        else:
            return False
    else:
        decimal_number = hexadecimal_to_decimal(number_16_8)
        return decimal_to_octal(decimal_number)


def decimal_to_hexadecimal(number_10_16):
    """
    To convert given number from decimal to hexadecimal
    :param number_10_16: (type=int) user provided number to be converted from decimal to hexadecimal
    :return: (type=str) hex number (as a module returns either hex number or false)
    """
    if __name__ != '__main__':
        if is_decimal(number_10_16):
            hex_number_10_16 = ""
            number_10_16 = int(number_10_16)
            while number_10_16 > 0:
                quotient = number_10_16 // 16
                remainder = number_10_16 % 16
                number_10_16 = int(quotient)
                while 15 < int(remainder):
                    remainder = remainder - 15
                if 0 < int(remainder) < 10:
                    hex_number_10_16 = str(int(remainder)) + hex_number_10_16
                elif int(remainder) == 10:
                    hex_number_10_16 = "A" + hex_number_10_16
                elif int(remainder) == 11:
                    hex_number_10_16 = "B" + hex_number_10_16
                elif int(remainder) == 12:
                    hex_number_10_16 = "C" + hex_number_10_16
                elif int(remainder) == 13:
                    hex_number_10_16 = "D" + hex_number_10_16
                elif int(remainder) == 14:
                    hex_number_10_16 = "E" + hex_number_10_16
                elif int(remainder) == 15:
                    hex_number_10_16 = "F" + hex_number_10_16
            return hex_number_10_16
        else:
            return False
    else:
        hex_number_10_16 = ""
        number_10_16 = int(number_10_16)
        while number_10_16 > 0:
            quotient = number_10_16 // 16
            remainder = number_10_16 % 16
            number_10_16 = int(quotient)
            while 15 < int(remainder):
                remainder = remainder - 15
            if 0 < int(remainder) < 10:
                hex_number_10_16 = str(int(remainder)) + hex_number_10_16
            elif int(remainder) == 10:
                hex_number_10_16 = "A" + hex_number_10_16
            elif int(remainder) == 11:
                hex_number_10_16 = "B" + hex_number_10_16
            elif int(remainder) == 12:
                hex_number_10_16 = "C" + hex_number_10_16
            elif int(remainder) == 13:
                hex_number_10_16 = "D" + hex_number_10_16
            elif int(remainder) == 14:
                hex_number_10_16 = "E" + hex_number_10_16
            elif int(remainder) == 15:
                hex_number_10_16 = "F" + hex_number_10_16
        return hex_number_10_16


def binary_to_hexadecimal(number_2_16):
    """
    To convert given number from binary to hexadecimal
    :param number_2_16: (type=str) user provided number to be converted from binary to hexadecimal
    :return: (type=str) hexadecimal number (as a module returns either hexadecimal number or false)
    """
    if __name__ != '__main__':
        if is_binary(number_2_16):
            decimal_number = binary_to_decimal(number_2_16)
            return decimal_to_hexadecimal(decimal_number)
        else:
            return False
    else:
        decimal_number = binary_to_decimal(number_2_16)
        return decimal_to_hexadecimal(decimal_number)


def octal_to_hexadecimal(number_8_16):
    """
    To convert given number from octal to hexadecimal
    :param number_8_16: (type=str) user provided number to be converted from octal to hexadecimal
    :return: (type=str) hexadecimal number (as a module returns either hexadecimal number or false)
    """
    if __name__ != '__main__':
        if is_octal(number_8_16):
            decimal_number = octal_to_decimal(number_8_16)
            return decimal_to_hexadecimal(decimal_number)
        else:
            return False
    else:
        decimal_number = octal_to_decimal(number_8_16)
        return decimal_to_hexadecimal(decimal_number)


def convertor(number_system):
    """
    convertor function which called and convert numbers from one number system to 3 other number system
    :param number_system: (expected input: B : Binary | O : Octal | D : Decimal | H : HexaDecimal)(type: str)
        based on input if user provides B that means he wants to convert from Binary to Decimal, Octal and Hexadecimal and print
        the output.
    :return:
    """
    if number_system.upper() == 'B':
        number = input("Please enter the Binary Number you want to convert:")
        if is_binary(number):
            print("#" * 50)
            decimal_number = binary_to_decimal(number)
            print(f"Decimal number of Binary({str(number)}) is {str(int(decimal_number))}")
            octal_number = decimal_to_octal(decimal_number)
            print(f"Octal number of Binary({str(number)}) is {str(int(octal_number))}")
            hex_number = decimal_to_hexadecimal(decimal_number)
            print(f"HexaDecimal number of Binary({str(number)}) is {str(hex_number)}")
            print("#" * 50)
            return 0
        else:
            print("Please enter valid Binary number or change the Number system and try again")
            return 0
    elif number_system.upper() == 'O':
        number = input("Please enter the Octal Number you want to convert:")
        if is_octal(number):
            print("#" * 50)
            decimal_number = octal_to_decimal(number)
            print(f"Decimal number of Octal({number}) is {str(int(decimal_number))}")
            binary_number = decimal_to_binary(decimal_number)
            print(f"Binary number of Octal({str(int(number))}) is {str(math.trunc(float(binary_number)))}")
            hex_number = decimal_to_hexadecimal(decimal_number)
            print(f"HexaDecimal number of Octal({str(int(number))}) is {str(hex_number)}")
            print("#" * 50)
            return 0
        else:
            print("Please enter valid Octal number or change the Number system and try again")
            return 0
    elif number_system.upper() == 'D':
        number = input("Please enter the Decimal Number you want to convert:")
        try:
            number = int(number)
            if is_decimal(number):
                print("#" * 50)
                octal_number = decimal_to_octal(number)
                print(f"Octal number of Decimal({number}) is {str(int(octal_number))}")
                binary_number = decimal_to_binary(number)
                print(f"Binary number of Decimal({str(int(number))}) is {str(math.trunc(float(binary_number)))}")
                hex_number = decimal_to_hexadecimal(number)
                print(f"HexaDecimal number of Decimal({str(int(number))}) is {str(hex_number)}")
                print("#" * 50)
                return 0
            else:
                print("Please enter valid Decimal number or change the Number system and try again")
                return 0
        except ValueError:
            print("An Error occurred!\nPlease enter valid Decimal number or change the Number system and try again")
    elif number_system.upper() == 'H':
        number = input("Please enter the Hexadecimal Number you want to convert:")
        if is_hex(number):
            print("#" * 50)
            decimal_number = hexadecimal_to_decimal(number)
            print(f"Decimal number of Hex({number}) is {str(int(decimal_number))}")
            octal_number = decimal_to_octal(decimal_number)
            print(f"Octal number of Hex({number}) is {str(int(octal_number))}")
            binary_number = decimal_to_binary(decimal_number)
            print(f"Binary number of Hex({str(number)}) is {str(binary_number)}")
            #
            print("#" * 50)
            return 0
        else:
            print("Please enter valid HexaDecimal number or change the Number system and try again")
            return 0
    else:
        print("Please make a valid choice: B/O/D/H")
        return 0


if __name__ == "__main__":
    while 1:
        print('+' * 50)
        number_system = input("Please select number-system of your number:\nB : Binary\nO : Octal\nD : Decimal\nH : "
                              "HexaDecimal\nE : Exit\nmake your choice:")
        print('+' * 50)
        if number_system.upper() == 'E':
            print("bye!" * 2)
            break
        else:
            convertor(number_system)
