import random


def conversion(number):
    def hexadecimalconv(number):
        hex_chars = "0123456789ABCDEF"
        hexadecimal_representation = ""
        while number > 0:
            remainder = number % 16
            hexadecimal_representation = hex_chars[remainder] + hexadecimal_representation
            number //= 16
        return hexadecimal_representation

    if 0 <= number <= 127:
        binary_representation = ""
        if number == 0:
            binary_representation = "0"
        while number > 0:
            binary_representation = str(number % 2) + binary_representation
            number //= 2
        return '-' + binary_representation if number < 0 else binary_representation
    else:
        return hexadecimalconv(number)


num = random.randint(0, 100000)

converted_value = conversion(num)
print("Random num:", num)
print("Converted num:", converted_value)
