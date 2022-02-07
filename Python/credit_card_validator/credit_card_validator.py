import re


def details():
    print(
        f"It must contain exactly 16 digits.\nIt should only contain 0-9 digits.\nIt must start with either 9 or 7 or "
        f"3.\nIt may have digits in a group of 4 with a separator (-).\nIt must not contain any other symbols such as _ "
        f"or space(‘ ‘).\n{'-' * 50}"
    )


def validate_card():
    card_number = input("Please enter the card number: ")

    pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    result = re.match(pattern, card_number)
    if result:
        print(card_number + "->" + "Valid card")
    else:
        print(card_number + "->" + "Invalid card")


if __name__ == "__main__":
    details()
    while 1:
        validate_card()
        another = input("Do you want to check another card (y/n):")
        if another == 'n':
            break
