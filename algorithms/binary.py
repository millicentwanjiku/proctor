"""Binary converter"""
def binary_converter(number):
    """A function that returns a binary number"""
    if number >= 0 and number <= 255:
        bina = str(bin(number))
        return bina[2:]
    else:
        return "Invalid input"
