import number_system_conversions

num = int(input('Please select your number: (Only decimal number) - '))
print(f"Binary of decimal number ({num}) is {number_system_conversions.decimal_to_binary(num)}")
print(f"Octal of decimal number ({num}) is {number_system_conversions.decimal_to_octal(num)}")
print(f"Hexadecimal of decimal number ({num}) is {number_system_conversions.decimal_to_hexadecimal(num)}")
