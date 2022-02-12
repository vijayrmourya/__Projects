- credit_card_validator.py : To validate the credit card number
- as_a_module.py : to test credit_card_validator.py as a python module

Code Output sample

## Output:

---
It must contain exactly 16 digits.

It should only contain 0-9 digits.

It must start with either 9 or 7 or 3.

It may have digits in a group of 4 with a separator (-).

It must not contain any other symbols such as _ or space(‘ ‘).

--------------------------------------------------
Please enter the card number: 1236547896523641

1236547896523641->Invalid card

---
Do you want to check another card (y/n):y

Please enter the card number: 9564123685745632

9564123685745632->Valid card

---
Do you want to check another card (y/n):985412_652362836

Exiting