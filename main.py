import random

def custom_conversion(number):
    if 0 <= number <= 255:
        binary_representation = ""
        if number == 0:
            binary_representation = "0"
        while number > 0:
            binary_representation = str(number % 2) + binary_representation
            number //= 2
        return '-' + binary_representation if number < 0 else binary_representation
    else:
        hexadecimal_representation = ""
        while number > 0:
            remainder = number % 16
            hexadecimal_representation = hex(remainder)[2:].upper() + hexadecimal_representation
            number //= 16
        return hexadecimal_representation

num = random.randint(-100000, 100000)

num1 = 12

converted_value = custom_conversion(num)
print("Random num:", num1)
print("Converted num:", converted_value)
