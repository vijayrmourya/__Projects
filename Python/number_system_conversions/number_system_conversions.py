import math


def is_binary(number_2):
    for i in number_2:
        if int(i) == 1 or int(i) == 0:
            continue
        else:
            return False
    return True


def is_octal(number_8):
    for i in number_8:
        if 0 <= int(i) <= 7:
            continue
        else:
            return False
    return True


def is_decimal(number_10):
    if number_10 % 1 == 0:
        return True
    else:
        return False


def is_hex(number_16):
    for i in number_16:
        if i == 'A' or i == 'B' or i == 'C' or i == 'D' or i == 'E' or i == 'F':
            continue
        elif 0 < int(i) < 9:
            continue
        else:
            return False
    return True


def binary_to_decimal(number_2_10):
    decimal_number_2_10 = 0
    power_2_10 = 0
    for i in number_2_10[::-1]:
        decimal_number_2_10 = decimal_number_2_10 + int(i) * math.pow(2, power_2_10)
        power_2_10 += 1
    return decimal_number_2_10


def octal_to_decimal(number_8_10):
    decimal_number_8_10 = 0
    power_8_10 = 0
    for i in number_8_10[::-1]:
        decimal_number_8_10 = decimal_number_8_10 + int(i) * math.pow(8, power_8_10)
        power_8_10 += 1
    return decimal_number_8_10


def hexadecimal_to_decimal(number_16_10):
    decimal_number_16_10 = 0
    power_16_10 = 0
    for i in number_16_10[::-1]:
        if i == 'A':
            decimal_number_16_10 += 10 * math.pow(16, power_16_10)
            power_16_10 += 1
        elif i == 'B':
            decimal_number_16_10 += 11 * math.pow(16, power_16_10)
            power_16_10 += 1
        elif i == 'C':
            decimal_number_16_10 += 12 * math.pow(16, power_16_10)
            power_16_10 += 1
        elif i == 'D':
            decimal_number_16_10 += 13 * math.pow(16, power_16_10)
            power_16_10 += 1
        elif i == 'E':
            decimal_number_16_10 += 14 * math.pow(16, power_16_10)
            power_16_10 += 1
        elif i == 'F':
            decimal_number_16_10 += 15 * math.pow(16, power_16_10)
            power_16_10 += 1
        else:
            decimal_number_16_10 += int(i) * math.pow(16, power_16_10)
            power_16_10 += 1
    return decimal_number_16_10


def decimal_to_binary(number_10_2):
    binary_number_10_2 = ''
    divisor_10_2 = 2
    while number_10_2 > 0:
        binary_number_10_2 = str(number_10_2 % divisor_10_2) + binary_number_10_2
        number_10_2 = int(number_10_2 // 2)
        if number_10_2 == 1:
            binary_number_10_2 = str(number_10_2) + binary_number_10_2
            number_10_2 = 0
    return binary_number_10_2


def decimal_to_octal(number_10_8):
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


def decimal_to_hexadecimal(number_10_16):
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


# Code starts here
while 1:
    number_system = input("Please select number system of your number:\nB : Binary\nO : Octal\nD : Decimal\nH : "
                          "Hex-Decimal\nE : Exit\nmake choice:")
    if number_system == 'E':
        print("Exiting!")
        break
    number = input("Please enter the number in same Number system of your choice:")
    if number_system == 'B':
        if is_binary(number):
            decimal_number = binary_to_decimal(number)
            print(f"Decimal number of Binary({str(number)}) is {str(int(decimal_number))}")
            octal_number = decimal_to_octal(decimal_number)
            print(f"Octal number of Binary({str(number)}) is {str(int(octal_number))}")
            hex_number = decimal_to_hexadecimal(decimal_number)
            print(f"Hex-Decimal number of Binary({str(number)}) is {str(hex_number)}")
        else:
            print("Please enter valid Binary number or change the Number system and try again")
    elif number_system == 'O':
        if is_octal(number):
            decimal_number = octal_to_decimal(number)
            print(f"Decimal number of Octal({number}) is {str(int(decimal_number))}")
            binary_number = decimal_to_binary(decimal_number)
            print(f"Binary number of Octal({str(int(number))}) is {str(math.trunc(float(binary_number)))}")
            hex_number = decimal_to_hexadecimal(decimal_number)
            print(f"Hex-Decimal number of Octal({str(int(number))}) is {str(hex_number)}")
        else:
            print("Please enter valid Octal number or change the Number system and try again")
    elif number_system == 'D':
        number = int(number)
        if is_decimal(number):
            octal_number = decimal_to_octal(number)
            print(f"Octal number of Decimal({number}) is {str(int(octal_number))}")
            binary_number = decimal_to_binary(number)
            print(f"Binary number of Decimal({str(int(number))}) is {str(math.trunc(float(binary_number)))}")
            hex_number = decimal_to_hexadecimal(number)
            print(f"Hex-Decimal number of Decimal({str(int(number))}) is {str(hex_number)}")
        else:
            print("Please enter valid Decimal number or change the Number system and try again")
    elif number_system == 'H':
        if is_hex(number):
            decimal_number = hexadecimal_to_decimal(number)
            print(f"Decimal number of Hex({number}) is {str(int(decimal_number))}")
            octal_number = decimal_to_octal(decimal_number)
            print(f"Octal number of Hex({number}) is {str(int(octal_number))}")
            binary_number = decimal_to_binary(decimal_number)
            print(f"Binary number of Hex({str(number)}) is {str(math.trunc(float(binary_number)))}")
        else:
            print("Please enter valid Hex-Decimal number or change the Number system and try again")
    else:
        print("Please make a valid choice")
